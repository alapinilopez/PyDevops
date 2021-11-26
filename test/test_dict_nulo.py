from src.dict_a_tabla import dict_a_tabla
import pytest


@pytest.mark.dict_nulo
def test_dict_nulo():
    assert dict_a_tabla({}) == "Su base de datos está vacía"
