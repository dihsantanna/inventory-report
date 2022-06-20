import csv
import json
import xml.etree.ElementTree as ET
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

        elif path.endswith(".json"):
            with open(path, encoding="utf-8") as file:
                product_list = json.load(file)

        elif path.endswith(".xml"):
            tree = ET.parse(path)
            root = tree.getroot()

            for child in root:
                product = dict()
                for attr in child:
                    product[attr.tag] = attr.text

                product_list.append(product)

        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)
