from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        data_list = []
        with open(path, "r") as file:
            data_reader = csv.DictReader(file, delimiter=",")
            for row in data_reader:
                data_list.append(row)

        if type == "simples":
            return SimpleReport.generate(data_list)

        if type == "completo":
            return CompleteReport.generate(data_list)
