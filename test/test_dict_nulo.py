from src.logic.dict_md import dict_md
import pytest


@pytest.mark.dict_nulo
def test_dict_nulo():
    assert dict_md({}) == "Su base de datos está vacía"
