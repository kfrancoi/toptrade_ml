import os

from src.helpers.utils import load_json


class Predictor(object):
    def __init__(self, model_path):
        # Report
        report_path = os.path.join(model_path, "report.json")
        self.__report = load_json(report_path)

        # Model version
        self.__model_version = "some-model-version"

    def get_report(self):
        return self.__report

    def predict(self, data):
        return {
            "data": data,
            "version": self.__model_version
        }
