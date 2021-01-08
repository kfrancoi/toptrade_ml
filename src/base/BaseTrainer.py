import abc
from copy import deepcopy
from typing import Any, Dict, Iterable


class BaseTrain(metaclass=abc.ABCMeta):
    def __init__(
        self, config: Dict[str, Any], model: Any, data: Iterable[Any]
    ) -> None:
        """Make this be a BaseTrain with the given parameters.

        BaseTrain are immutable objects.

        Args:
            config: the configuration of the trainer
            model: the model for the trainer
            data: the data for the training

        Requires:
            no parameter is None

        """
        assert config is not None
        assert model is not None
        assert data is not None

        self.__config = config
        self.__model = model
        self.__data = data

    @property
    def config(self) -> Dict[str, Any]:
        """Return a copy of the configuration of this trainer.

        Returns:
            a copy of the configuration of this trainer

        """
        return deepcopy(self.__config)

    @property
    def model(self) -> Any:
        """Return the model for this trainer.

        Returns:
            the model for this trainer

        """
        return self.__model

    @property
    def data(self) -> Iterable[Any]:
        """Return a copy of the training data of this trainer.

        Returns:
            the training data of this trainer

        """
        return deepcopy(self.__data)

    @abc.abstractmethod
    def train(self) -> None:
        """Train the model on the training data.

        Effects:
            The model is trained on the data

        """
        raise NotImplementedError
