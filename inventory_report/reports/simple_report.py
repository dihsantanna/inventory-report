from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list: list):
        oldest_date = min(item["data_de_fabricacao"] for item in list)

        closest_date = min(item["data_de_validade"] for item in list)

        company = Counter(
            item["nome_da_empresa"] for item in list
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
