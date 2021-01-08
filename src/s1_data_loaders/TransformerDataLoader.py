from typing import Any, Dict

from src.base.BaseDataLoader import BaseDataLoader


class TransformerDataLoader(BaseDataLoader):
    def __init__(self, config: Dict[str, Any]) -> None:
        """Make this be a new TransformerDataLoader with the given configuration.

        It is worth noting that the configuration of self is immutable.

        Args:
            config: The given configuration

        Requires:
            configuration is not None

        Effects:
            Initialize this

        """
        super().__init__(config["data"])

        print("Loading dataframe...")
        self.__load()
        print("Splitting dataframe...")
        self.__split()

    def train_data(self):  # noqa: D102
        return {
            "X": [],
            "y": []
        }

    def test_data(self):  # noqa: D102
        return {
            "X": [],
            "y": []
        }

    def __load(self):
        pass

    def __split(self):
        pass
