from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(self, path, report):
        if "csv" in path:
            report_data = CsvImporter.import_data(path)

        if "json" in path:
            report_data = JsonImporter.import_data(path)

        if "xml" in path:
            report_data = XmlImporter.import_data(path)

        if report == "simples":
            return SimpleReport.generate(report_data)

        return CompleteReport.generate(report_data)
