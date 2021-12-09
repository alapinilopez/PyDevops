from src.logic.cars_year_md import cars_classics_md
from tests import *
import pytest



@pytest.mark.year
def test_correcto():
    assert cars_classics_md(doc_correct_classic) == '* **model**: mustang\n* **brand**: ford\n* **passengers**: 5\n* **year**: 1998\n* **price**: 65\n* **available**: True\n\n'
