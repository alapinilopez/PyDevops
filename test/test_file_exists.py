from src.logic.write_cars_all import check_file_exists
import pytest

file_path_correct = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\main.md"
file_path_incorrect = r"C:\Users\asorp\Documents\proyecto\PyDevops\PyDevops\hugo\Sites\carrenting\content\incorrect.md"

@pytest.mark.file_exists
def test_path_correct():
    assert check_file_exists(file_path_correct) == True

@pytest.mark.file_exists
def test_path_incorrect():
    assert check_file_exists(file_path_incorrect) == False