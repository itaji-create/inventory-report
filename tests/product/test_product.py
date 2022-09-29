from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "livro",
        "dono do livro",
        "2012/12/12",
        "2013/12/13",
        "BR85 2004 2335",
        "qualquer lugar"
    )
    assert type(product.id) is int
    assert product.nome_do_produto == "livro"
    assert product.nome_da_empresa == "dono do livro"
    assert product.data_de_fabricacao == "2012/12/12"
    assert product.data_de_validade == "2013/12/13"
    assert product.numero_de_serie == "BR85 2004 2335"
    assert product.instrucoes_de_armazenamento == "qualquer lugar"
