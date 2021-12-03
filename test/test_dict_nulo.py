from src.logic.cars_all_md import cars_all_md
import pytest


@pytest.mark.dict_nulo
def test_dict_nulo():
    assert cars_all_md({}) == "Su base de datos está vacía"
