import abc
from copy import deepcopy
from typing import Any, Dict, Iterable


class BaseEvaluater(metaclass=abc.ABCMeta):
    def __init__(self, model: Any, data: Iterable[Any]):
        """Make this be a BaseEvaluater.

        Args:
            model: the model
            data: the data for the evaluation

        Requires:
            model is not None and data is not None

        """
        assert model is not None
        assert data is not None

        self.__model = model
        self.__data = data

    @property
    def model(self) -> Any:
        """Return the model used in the evaluator.

        Returns:
            The model of this evaluator

        """
        return self.__model

    @property
    def data(self) -> Iterable[Any]:
        """Return a copy of the data in self.

        Returns:
            A copy of the evaluation data

        """
        return deepcopy(self.__data)

    @abc.abstractmethod
    def score(self) -> float:
        """Return the score of this model.

        Returns:
            a float value (between 0 and 1) representing
            the score of the model

        """
        raise NotImplementedError

    @abc.abstractmethod
    def summary(self) -> Dict[str, Any]:
        """Return a summary of this model.

        This summary represents the configuration of this model
        for this expériement

        Returns:
            a dictionnary representing the configuration for this
            model

        """
        raise NotImplementedError
