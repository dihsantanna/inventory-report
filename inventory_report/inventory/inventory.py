import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def generate_report_by_type(cls, type, product_list):
        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)

    @classmethod
    def import_data(cls, path, type):
        product_list = list()

        with open(path, encoding="utf-8") as file:
            if path.endswith(".csv"):
                reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *rows = reader
                product_list = list(dict(zip(header, row)) for row in rows)

            elif path.endswith(".json"):
                product_list = json.load(file)

            elif path.endswith(".xml"):
                products = xmltodict.parse(file.read())["dataset"]["record"]
                product_list = products

        return cls.generate_report_by_type(type, product_list)
