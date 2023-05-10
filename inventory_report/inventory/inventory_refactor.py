from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        data_list = self.importer.import_data(path)
        self.data.extend(data_list)
        if type == "simples":
            return SimpleReport.generate(data_list)
        else:
            return CompleteReport.generate(data_list)

    def __iter__(self):
        return InventoryIterator(self.data)

    # @staticmethod
    # def json_data(file):
    #     list = json.load(file)
    #     return list

    # @staticmethod
    # def data_type(path, file_extension):
    #     data_list = []
    #     with open(path, "r") as file:
    #         if file_extension == ".csv":
    #             data_reader = csv.DictReader(file, delimiter=",")
    #             for row in data_reader:
    #                 data_list.append(row)

    #         if file_extension == ".json":
    #             data_list = InventoryRefactor.json_data(file)

    #         if file_extension == ".xml":
    #             pre_list = xmltodict.parse(file.read())
    #             data_list = pre_list["dataset"]["record"]
    #     return data_list

    # @staticmethod
    # def import_data(path, type):
    #     filename, file_extension = os.path.splitext(path)

    #     data_list = InventoryRefactor.data_type(path, file_extension)

    #     if type == "simples":
    #         return SimpleReport.generate(data_list)

    #     if type == "completo":
    #         return CompleteReport.generate(data_list)
