from src.BBDD_access.BBDD_connect import *
import pytest

uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'
uri_incorrect = 'mongodb+srv://admin:incorrectpassword@cluster0.thpbm.mongodb.net/PyDevops?retryWrites=true&w=majority'

@pytest.mark.BBDD_connect
def test_correct_uri():
    assert connection(uri) == True

# Esta función es solo para checkear que, si la uri es incorrecta, no se conecta a la BBDD.
# Es solo para el caso test, no se enviará a producción, ya que si no se conecta queremos que pare el programa (exit)
# Y con el return solo para esa función
def invalid_uri(uri): 
    try:
        client = pymongo.MongoClient(uri)
        client.server_info()
    except:
        return False

@pytest.mark.BBDD_connect
def test_incorrect_uri():
    assert invalid_uri(uri_incorrect) == False

