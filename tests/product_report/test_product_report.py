from inventory_report.inventory.product import Product

product_mock = {
    "id": 10,
    "nome_do_produto": "anel de poder",
    "nome_da_empresa": "Sauron ltda",
    "data_de_fabricacao": "2019-04-15",
    "data_de_validade": "2022-06-22",
    "numero_de_serie": "012345678",
    "instrucoes_de_armazenamento": "no fundo de lagos",
}

report = (
    f"O produto {product_mock['nome_do_produto']}"
    f" fabricado em {product_mock['data_de_fabricacao']}"
    f" por {product_mock['nome_da_empresa']}"
    f" com validade até {product_mock['data_de_validade']}"
    f" precisa ser armazenado {product_mock['instrucoes_de_armazenamento']}."
)


def test_relatorio_produto():
    prod = Product(**product_mock)
    assert repr(prod) == report
