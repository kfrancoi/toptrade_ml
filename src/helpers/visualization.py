import io
import itertools
import os

import keras
import matplotlib
import numpy as np
import sklearn
import tensorflow as tf
from src.helpers.utils import create_dir

matplotlib.use("Agg")
"""
Add :
tensorflow(-gpu)==2.0.0
Tensorboard==2.0.0
keras ==2.3.0


ADD THIS IN YOUR NOTEBOOK
import os
os.chdir("/home/jovyan/")
def load_tensorboard(experiment_time):
    log_dir = "data/saved/tensorboard_logs/"+experiment_time
    %reload_ext tensorboard
    %tensorboard --logdir {log_dir} --host 0.0.0.0
    from tensorboard import notebook
    notebook.display(port=6006, height=1000)
"""


def callback_tensorboard(val_data, loss_fct, experiment_time, class_names):
    """
    Args :
        val_data : validation data. Either a generator or of form X,y
        loss_fct : string : Keras loss function
        experiment_time : str of time. Used to create subdirectory to store the
            tensorboard data
        class_names: list of strings. Put None if not a classification problem.
    """
    log_dir = os.path.join("data/saved/tensorboard_logs", experiment_time)
    create_dir(log_dir)
    tensorboard_callback = ExtendedTensorBoard(
        val_data,
        loss_fct,
        class_names,
        log_dir=log_dir,
        histogram_freq=1,
        profile_batch=0,
        write_graph=True,
        write_images=True,
    )
    return tensorboard_callback


class ExtendedTensorBoard(keras.callbacks.TensorBoard):
    def __init__(self, val_data, loss_fct, class_names, **kwargs):

        super().__init__(**kwargs)
        self.validation_data = val_data
        self.loss_fct = keras.losses.get(loss_fct)
        self.current_epoch = tf.Variable(0, dtype="int64")
        self.class_names = class_names

    @tf.function
    @tf.autograph.experimental.do_not_convert()
    def _log_gradients(self):

        writer = self._get_writer(self._train_run_name)

        with writer.as_default():
            # here we use validation data to calculate the gradients
            try:
                _x_batch, y_true = self.validation_data.__getitem__(0)
            except Exception:
                _x_batch, y_true = self.validation_data
            _x_batch = tf.convert_to_tensor(_x_batch)
            _y_pred = self.model(_x_batch)  # forward-propagation
            y_true = self.reshape(y_true, _y_pred)

            loss = self.loss_fct(
                y_true=y_true, y_pred=_y_pred
            )  # calculate loss
            gradients = self.model.optimizer.get_gradients(
                loss, self.model.trainable_weights
            )  # back-propagation

            # In eager mode, grads does not have name, so we get names from
            #  model.trainable_weights
            for weights, grads in zip(self.model.trainable_weights, gradients):
                name = weights.name.replace(":", "_") + "_grads"
                tf.summary.histogram(name, data=grads, step=self.current_epoch)

        writer.flush()

    def log_confusion_matrix(self, epoch, logs):
        # Use the model to predict the values from the validation dataset.
        _x_batch, y_true = self.validation_data.__getitem__(0)
        test_pred_raw = self.model.predict(_x_batch)
        if len(self.class_names) > 2:
            test_pred = np.argmax(test_pred_raw, axis=1)
        else:
            test_pred = [1 if i > 0.5 else 0 for i in test_pred_raw]

        # Calculate the confusion matrix.
        cm = sklearn.metrics.confusion_matrix(y_true, test_pred)
        # Log the confusion matrix as an image summary.
        figure = self.plot_confusion_matrix(cm)
        cm_image = self.plot_to_image(figure)

        # Log the confusion matrix as an image summary.
        writer = self._get_writer(self._train_run_name)
        with writer.as_default():
            tf.summary.image("Confusion Matrix", cm_image, step=epoch)

    def on_epoch_end(self, epoch, logs=None):
        # This function overwrites the on_epoch_end in
        # tf.keras.callbacks.TensorBoard
        # but we do need to run the original on_epoch_end, so here we use the
        # super function.
        super(ExtendedTensorBoard, self).on_epoch_end(epoch, logs=logs)
        if self.class_names is not None:
            self.log_confusion_matrix(epoch, logs)
        if self.histogram_freq and epoch % self.histogram_freq == 0:
            self.current_epoch.assign(epoch)
            tf.function(self._log_gradients())

    def reshape(self, y_true, y_pred):
        """
        Model can return predicitons of shape (batch_size,) and not explicitly
        show other dimensions.
        This causes error in the loss fct.
        """
        reshaped = np.zeros(y_pred.shape)
        for i in range(len(reshaped)):
            reshaped[i] = y_true[i]
        return reshaped

    def plot_confusion_matrix(self, cm):
        """
        Returns a matplotlib figure containing the plotted confusion matrix.

        Args:
            cm (array, shape = [n, n]): a confusion matrix of integer classes
            class_names (array, shape = [n]): String names of the integer
            classes
        """
        import matplotlib.pyplot as plt

        figure = plt.figure(figsize=(8, 8))
        plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
        plt.title("Confusion matrix")
        plt.colorbar()
        tick_marks = np.arange(len(self.class_names))
        plt.xticks(tick_marks, self.class_names, rotation=45)
        plt.yticks(tick_marks, self.class_names)

        # Normalize the confusion matrix.
        cm = np.around(
            cm.astype("float") / cm.sum(axis=1)[:, np.newaxis], decimals=2
        )

        # Use white text if squares are dark; otherwise black.
        threshold = cm.max() / 2.0
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            color = "white" if cm[i, j] > threshold else "black"
            plt.text(j, i, cm[i, j], horizontalalignment="center", color=color)

        plt.tight_layout()
        plt.ylabel("True label")
        plt.xlabel("Predicted label")
        return figure

    def plot_to_image(self, figure):
        """Converts the matplotlib plot specified by 'figure' to a PNG image and
        returns it. The supplied figure is closed and inaccessible after this
        call."""
        # Save the plot to a PNG in memory.
        import matplotlib.pyplot as plt

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        # Closing the figure prevents it from being displayed directly inside
        # the notebook.
        plt.close(figure)
        buf.seek(0)
        # Convert PNG buffer to TF image
        image = tf.image.decode_png(buf.getvalue(), channels=4)
        # Add the batch dimension
        image = tf.expand_dims(image, 0)
        return image
