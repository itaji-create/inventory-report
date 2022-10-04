from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, params):
        datas_fabricacao = [item["data_de_fabricacao"] for item in params]
        datas_validade = [item["data_de_validade"] for item in params]
        companies = [item["nome_da_empresa"] for item in params]

        company_most_common = Counter(companies).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(datas_fabricacao)}\n"
            f"Data de validade mais próxima: {min(datas_validade)}\n"
            f"Empresa com mais produtos: {company_most_common}"
        )
