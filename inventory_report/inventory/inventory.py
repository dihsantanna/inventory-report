import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        product_list = list()

        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *rows = reader
                product_list = list(dict(zip(header, row)) for row in rows)

        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
