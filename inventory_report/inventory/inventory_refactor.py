from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from .inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report):
        data = self.importer.import_data(path)
        for product in data:
            self.data.append(product)
        if report == "simples":
            return SimpleReport.generate(self.data)

        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
