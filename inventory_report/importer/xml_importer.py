from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            data_list = xmltodict.parse(file.read())
            return data_list["dataset"]["record"]
