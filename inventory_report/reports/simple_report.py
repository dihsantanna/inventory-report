class SimpleReport:
    @staticmethod
    def generate(list: list):
        oldest_date = min(item["data_de_fabricacao"] for item in list)

        closest_date = min(item["data_de_validade"] for item in list)

        companies = [comp["nome_da_empresa"] for comp in list]
        company = ""
        memory = []
        memoryCount = 0

        for item in companies:
            if item in memory:
                continue

            count = companies.count(item)

            if count > memoryCount:
                memoryCount = count
                company = item
            memory.append(item)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )
