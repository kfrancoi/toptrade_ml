import abc
from copy import deepcopy
from typing import Any, Dict, Iterable


class BaseModel(metaclass=abc.ABCMeta):
    def __init__(self, config: Dict[str, Any]):
        """Make this be a BaseModel with the given configuration.

        BaseModel is an immutable object.

        Args:
            config: the configuration for the model

        Requires:
            config is not None

        """
        assert config is not None
        self.__config = config

    @property
    def config(self) -> Dict[str, Any]:
        """Return the configuration of this model.

        The returned configurtion is a copy of the original
        one

        Returns:
            a copy of the configuration for this model

        """
        return deepcopy(self.__config)

    @abc.abstractmethod
    def build(self) -> None:
        """Build the model.

        Effects:
            The model is build and ready to use

        """
        raise NotImplementedError

    @abc.abstractmethod
    def predict(self, data: Iterable[Any]) -> Iterable[Any]:
        """Make predictions with the model.

        Args:
            data: An iterable of examples to be predicted

        Requires:
            data is not None

        Returns:
            An iterable of prediction for the input examples

        """
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, model_path: str) -> None:
        """Save the model to a file.

        Args:
            model_path: the path where the model must be saved

        Requires:
            model_path is not None and is a valid path

        """
        raise NotImplementedError
