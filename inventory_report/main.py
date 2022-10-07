import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    _, path, type = sys.argv

    if '.csv' in sys.argv[1]:
        data_type = InventoryRefactor(CsvImporter)
    if '.json' in sys.argv[1]:
        data_type = InventoryRefactor(JsonImporter)
    if '.xml' in sys.argv[1]:
        data_type = InventoryRefactor(XmlImporter)

    return sys.stdout.write(data_type.import_data(path, type))
