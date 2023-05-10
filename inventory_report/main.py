import sys
from inventory_report.inventory.inventory import Inventory


def main():
    try:
        path, type = sys.argv[1:]
        report = Inventory.import_data(path, type)

        sys.stdout.write(report)

    except (IndexError, KeyError, ValueError):
        sys.stderr.write("Verifique os argumentos\n")
