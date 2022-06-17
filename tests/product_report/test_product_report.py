from typing import cast
from inventory_report.inventory.product import Product

assert_product = (
    "O produto Biscoito Recheado de Limão"
    + " fabricado em 17-06-2022"
    + " por Piraquê"
    + " com validade até 17-12-2022"
    + " precisa ser armazenado em local seco e arejado."
)


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="Biscoito Recheado de Limão",
        nome_da_empresa="Piraquê",
        data_de_fabricacao="17-06-2022",
        data_de_validade="17-12-2022",
        numero_de_serie="12345678",
        instrucoes_de_armazenamento="em local seco e arejado",
    )

    assert str(cast(typ=str, val=product)) == assert_product
