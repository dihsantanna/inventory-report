from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Biscoito Recheado de Limão",
        nome_da_empresa="Piraquê",
        data_de_fabricacao="17-06-2022",
        data_de_validade="17-12-2022",
        numero_de_serie="12345678",
        instrucoes_de_armazenamento="Local seco e arejado",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Biscoito Recheado de Limão"
    assert product.nome_da_empresa == "Piraquê"
    assert product.data_de_fabricacao == "17-06-2022"
    assert product.data_de_validade == "17-12-2022"
    assert product.numero_de_serie == "12345678"
    assert product.instrucoes_de_armazenamento == "Local seco e arejado"
