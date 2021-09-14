# para ejecutar la prueba se pone pytest en la consola
from numeros import programa

def test_answer():
    assert programa(3) == "tres"