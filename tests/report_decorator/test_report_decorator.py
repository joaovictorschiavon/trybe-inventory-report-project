from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

FINISH_DECO = "\033[0m"
BLUE_DECO = "\033[36m"
GREEN_DECOR = "\033[32m"
RED_DECO = "\033[31m"

mock_list = [
    {
        "id": 10,
        "nome_do_produto": "anel de poder",
        "nome_da_empresa": "Sauron ltda",
        "data_de_fabricacao": "2019-04-15",
        "data_de_validade": "2025-06-22",
        "numero_de_serie": "012345678",
        "instrucoes_de_armazenamento": "no fundo de lagos",
    }
]

FABRICATION_DATE = mock_list[0]["data_de_fabricacao"]
EXPIRATION_DATE = mock_list[0]["data_de_validade"]
COMPANY_NAME = mock_list[0]["nome_da_empresa"]
var1 = f"{GREEN_DECOR}Data de fabricação mais antiga:{FINISH_DECO}"
var2 = f"{GREEN_DECOR}Data de validade mais próxima:{FINISH_DECO}"
var3 = f"{GREEN_DECOR}Empresa com mais produtos:{FINISH_DECO}"

expected_report = (
    f"{var1} {BLUE_DECO}{FABRICATION_DATE}{FINISH_DECO}\n"
    f"{var2} {BLUE_DECO}{EXPIRATION_DATE}{FINISH_DECO}\n"
    f"{var3} {RED_DECO}{COMPANY_NAME}{FINISH_DECO}"
)


def test_decorar_relatorio():
    assert (ColoredReport(SimpleReport).generate(mock_list)) == expected_report
