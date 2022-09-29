from collections import Counter


class SimpleReport:
    def generate(params):
        datas_fabricacao = [item["data_de_fabricacao"] for item in params]
        datas_validade = [item["data_de_validade"] for item in params]
        empresas = [item["nome_da_empresa"] for item in params]

        empresa_most_common = Counter(empresas).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(datas_fabricacao)}\n"
            f"Data de validade mais próxima: {min(datas_validade)}\n"
            f"Empresa com mais produtos: {empresa_most_common}"
        )
