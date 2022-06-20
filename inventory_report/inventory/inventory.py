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

        if path.endswith(".csv"):
            with open(path, encoding="utf-8") as file:
                reader = csv.reader(file, delimiter=",", quotechar='"')
                header, *rows = reader
                product_list = list(dict(zip(header, row)) for row in rows)

        elif path.endswith(".json"):
            with open(path, encoding="utf-8") as file:
                product_list = json.load(file)

        elif path.endswith(".xml"):
            with open(path, encoding="utf-8") as file:
                products = xmltodict.parse(file.read())["dataset"]["record"]
                product_list = products

        return cls.generate_report_by_type(type, product_list)
