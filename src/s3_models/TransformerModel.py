from typing import Any, Dict, Iterable

from src.base.BaseModel import BaseModel


class TransformerModel(BaseModel):
    def __init__(self, config: Dict[str, Any]):
        """Make this be a new TransformerModel.

        Args:
            config: the configuration for this model

        Requires:
            config is not None

        """
        super().__init__(config["model"])

        self.__model = None

        self.build()

    @property
    def model(self) -> Any:
        """Return the inner library specific model.

        Returns:
            the inner library specific model

        """
        return self.__model

    def predict(self, data: Iterable[Any]) -> Iterable[Any]:  # noqa: D102
        if self.__model is None:
            raise Exception("You have to build the model first.")
        # TODO implement your model prediction

    def save(self, model_path: str) -> None:  # noqa: D102
        if self.__model is None:
            raise Exception("You have to build the model first.")
        # TODO implement your model saving

    def build(self) -> None:  # noqa: D102
        # TODO implement your model
        self.__model = {}
