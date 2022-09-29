from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "BR85 2004 2335",
        "ao abrigo de luz"
    )
    f = "O produto farinha fabricado em 01-05-2021 por Farinini "
    f2 = "com validade até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    assert str(product) == f + f2
