from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: list):
        qty_of_products_per_company = Counter(
            item["nome_da_empresa"] for item in list
        ).most_common()

        qty_of_products_per_company_str = ""

        for company, qty in qty_of_products_per_company:
            qty_of_products_per_company_str += f"- {company}: {qty}\n"

        return (
            f"{SimpleReport.generate(list)}\n"
            "Produtos estocados por empresa:\n"
            f"{qty_of_products_per_company_str}"
        )
