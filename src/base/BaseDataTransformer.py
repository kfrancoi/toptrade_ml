import abc
from copy import deepcopy
from typing import Any, Dict, Iterable


class BaseDataTransformer(metaclass=abc.ABCMeta):
    def __init__(self, config: Dict[str, Any], data: Iterable[Any]) -> None:
        """Make this be a new Transformer with the given configuration.

        It is worth noting that the configuration of self is immutable.

        Args:
            config: The given configuration
            data: The data to transform

        Requires:
            config is not None
            data is not None

        Effects:
            Initialize this

        """
        assert config is not None
        assert data is not None

        self.__config = config
        self.__data = data

    @property
    def config(self) -> Dict[str, Any]:
        """Return a copy of the configuration.

        Returns:
            a copy of the configuration

        """
        return deepcopy(self.__config)

    @property
    def data(self) -> Iterable[Any]:
        """Return a copy of the data of this transformer.

        Returns:
            the data of this transformer

        """
        return deepcopy(self.__data)

    @abc.abstractmethod
    def get_transformed_data(self) -> Iterable[Any]:
        """Return the transformed data.

        Returns:
            An iterable object containing training examples

        """
        raise NotImplementedError
