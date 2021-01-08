from typing import Any, Dict, Iterable

from src.base.BaseEvaluater import BaseEvaluater


class TransformerEvaluater(BaseEvaluater):
    def __init__(self, model: Any, data: Iterable[Any]):
        """Make this be a TransformerEvaluater.

        Args:
            model: the model
            data: the data for the evaluation

        Requires:
            model is not None and data is not None

        """
        super().__init__(model, data)

        self.__score = None
        self.__summary = None

        self.calculate_scores()

    def score(self) -> float:  # noqa: D102
        return self.__score

    def summary(self) -> Dict[str, Any]:  # noqa: D102
        return self.__summary

    def calculate_scores(self):
        self.__score = 0
        self.__summary = {
            "score": self.__score
        }
