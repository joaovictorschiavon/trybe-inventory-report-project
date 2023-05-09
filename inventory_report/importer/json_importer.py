from .importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            data_list = json.load(file)
            return data_list
