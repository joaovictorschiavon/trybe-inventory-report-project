from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        "2",
        "mock_product",
        "mock_company",
        "2020-01-01",
        "2025-01-01",
        "0123456789",
        "O produto de deve ser guardado",
    )
    assert product.id == "2"
    assert product.nome_da_empresa == "mock_company"
    assert product.nome_do_produto == "mock_product"
    assert product.data_de_fabricacao == "2020-01-01"
    assert product.data_de_validade == "2025-01-01"
    assert product.numero_de_serie == "0123456789"
    assert (
        product.instrucoes_de_armazenamento == "O produto de deve ser guardado"
    )
