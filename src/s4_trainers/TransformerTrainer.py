import time
from typing import Any, Dict, Union

from src.base.BaseTrainer import BaseTrain


class TransformerTrainer(BaseTrain):
    def __init__(
        self,
        config: Dict[str, Any],
        model: Any,
        data: Any,
        experiment_time: Union[str, None] = None,
    ):
        """Make this be a new TransformerTrainer
        with the specified parameters.

        Args:
            config: the configuration of the trainer
            model: the model to be trained
            data: the data for the training
            experiment_time: optionnal time for the experiment

        Requires:
            config, model and data is not None

        """
        super().__init__(config["train"], model, data)

        self.experiments_name = config["name"]
        self.experiment_time = experiment_time
        if self.experiment_time is None:
            self.experiment_time = time.strftime(
                "%Y-%m-%d:%Hh%M", time.localtime()
            )

    def train(self):  # noqa: D102
        # TODO implement training
        pass
