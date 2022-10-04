from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, params):
        simple_report = super().generate(params)
        companies = [item["nome_da_empresa"] for item in params]

        company_most_common = Counter(companies).most_common()
        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{self.company_quantity(company_most_common)}"
        )

    def company_quantity(list):
        result = ""
        for item in list:
            result += f"- {item[0]}: {item[1]}\n"
        return result
