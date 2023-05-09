from .importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        data_list = []
        with open(path, "r") as file:
            data_reader = csv.DictReader(file, delimiter=",")
            for row in data_reader:
                data_list.append(row)
        return data_list
