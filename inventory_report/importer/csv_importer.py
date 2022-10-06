from abc import abstractmethod
import csv


from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @abstractmethod
    def import_data(path: str):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        try:
            with open(path) as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
