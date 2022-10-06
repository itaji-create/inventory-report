import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

# from inventory_report.importer.importer import Importer
# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def csv_reader(path):
        with open(path) as file:
            reader = list(csv.DictReader(file))
            return reader

    def json_reader(path):
        with open(path) as file:
            reader = json.load(file)
            return reader

    def xml_reader(path):
        with open(path) as file:
            reader = xmltodict.parse(file.read())["dataset"]["record"]
            return list(reader)

    @classmethod
    def import_data(self, path, report):
        if "csv" in path:
            report_data = self.csv_reader(path)

        if "json" in path:
            report_data = self.json_reader(path)

        if "xml" in path:
            report_data = self.xml_reader(path)

        if report == "simples":
            return SimpleReport.generate(report_data)

        return CompleteReport.generate(report_data)
