from src.logic.hugo_run import *
import pytest


@pytest.mark.hugo_installed
def test_correct_installation():
    assert check_hugo_installed() == True