from abc import abstractmethod
import json


from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @abstractmethod
    def import_data(path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        try:
            with open(path) as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
