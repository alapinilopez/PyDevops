from src.logic.cars_lte_md import cars_cheaper_md
from tests import *
import pytest


@pytest.mark.price
def test_correcto():
    assert cars_cheaper_md(doc_correct) == '\n### Item 1\n* model: clio\n* brand: renault\n* category:\n* * name: common\n* * discountTax: 60\n* passengers: 5\n* year: 2018\n* **price: 20**\n* available: True\n'

@pytest.mark.price
def test_incorrecto1():
    assert not cars_cheaper_md(doc_incorrect1) == '* **model**: clio\n* **brand**: renault\n* **passengers**: 5\n* **year**: 2018\n* **price**: 20\n* **available**: True\n\n'
