from ..reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        self.new_dict = self.new_dict

    @staticmethod
    def generate(list):
        # dict_of_report = CompleteReport.new_dict
        # this_set = set([x[0] for x in dict_of_report])
        # print(this_set, "set")
        # final_dict = dict([{y: 0} for y in this_set])
        # answer = "Produtos estocados por empresa:\n"
        # for x in this_set:
        #     for item in dict_of_report:
        #         if x == item["nome_da_empresa"]:
        #             final_dict[x] += 1
        count_companies = dict()
        for item in list:
            if item['nome_da_empresa'] not in count_companies:
                count_companies[item['nome_da_empresa']] = 1
            else:
                count_companies[item['nome_da_empresa']] += 1
        answer = "\nProdutos estocados por empresa:\n"
        for h in count_companies.items():
            answer += f"- {h[0]}: {h[1]}\n"
        teste = SimpleReport.generate(list)
        final = teste + answer
        return final
