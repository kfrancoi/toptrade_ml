from typing import Any, Dict, Iterable

from src.base.BaseDataTransformer import BaseDataTransformer


class TransformerDataTransformer(BaseDataTransformer):
    def __init__(self, config: Dict[str, Any], data: Iterable[Any]) -> None:
        """Make this be a new Data Transformer with the given configuration.

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
        super().__init__(config["transform"], data)
        self.transformed_data = None

        self.__transform()

    def get_transformed_data(self):  # noqa: D102
        return self.transformed_data

    def __transform(self):
        self.transformed_data = self.data
