import abc
from copy import deepcopy
from typing import Any, Dict, Iterable


class BaseDataLoader(metaclass=abc.ABCMeta):
    def __init__(self, config: Dict[str, Any]) -> None:
        """Make this be a new DataLoader with the given configuration.

        It is worth noting that the configuration of self is immutable.

        Args:
            config: The given configuration

        Requires:
            config is not None

        Effects:
            Initialize this

        """
        assert config is not None

        self.__config = config

    @property
    def config(self) -> Dict[str, Any]:
        """Return a copy of the configuration.

        Returns:
            a copy of the configuration

        """
        return deepcopy(self.__config)

    @abc.abstractmethod
    def train_data(self) -> Iterable[Any]:
        """Return the training data.

        Returns:
            An iterable object containing training examples

        """
        raise NotImplementedError

    @abc.abstractmethod
    def test_data(self) -> Iterable[Any]:
        """Return the test data.

        Returns:
            An iterable object containing test examples

        """
        raise NotImplementedError
