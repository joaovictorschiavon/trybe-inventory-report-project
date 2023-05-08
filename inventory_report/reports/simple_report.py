from datetime import datetime


class SimpleReport:
    @staticmethod
    def str_to_date(x):
        if isinstance(x, str):
            return datetime.strptime(x, "%Y-%m-%d").date()
        else:
            return x

    fabrication_date = datetime.now().date()
    expiration_date = datetime.max.date()
    new_dict = dict()
    most_products_company = ""
    most_product_number = 0

    @staticmethod
    def company_count():
        for y in __class__.new_dict.items():
            if int(y[1] > __class__.most_product_number):
                __class__.most_products_company = y[0]
                __class__.most_product_number = int(y[1])

    @staticmethod
    def datetime_to_str(k):
        return datetime.strftime(k, "%Y-%m-%d")

    @staticmethod
    def generate(list):
        for item in list:
            if __class__.str_to_date(
                item["data_de_fabricacao"]
            ) < __class__.str_to_date(__class__.fabrication_date):
                __class__.fabrication_date = __class__.str_to_date(
                    item["data_de_fabricacao"]
                )
            if (
                __class__.str_to_date(datetime.now().date())
                < __class__.str_to_date(item["data_de_validade"])
                < __class__.str_to_date(__class__.expiration_date)
            ):
                __class__.expiration_date = __class__.str_to_date(
                    item["data_de_validade"]
                )
            if item["nome_da_empresa"] in __class__.new_dict:
                __class__.new_dict[item["nome_da_empresa"]] += 1
            else:
                __class__.new_dict[item["nome_da_empresa"]] = 1
            __class__.company_count()

        return (
            "Data de fabricação mais antiga:"
            + f" {__class__.datetime_to_str(__class__.fabrication_date)}\n"
            + "Data de validade mais próxima:"
            + f" {__class__.datetime_to_str(__class__.expiration_date)}\n"
            + f"Empresa com mais produtos: {__class__.most_products_company}"
        )
