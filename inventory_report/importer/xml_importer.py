from abc import abstractmethod
import xmltodict


from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @abstractmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        try:
            with open(path) as file:
                reader = xmltodict.parse(file.read())["dataset"]["record"]
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: {path}")
