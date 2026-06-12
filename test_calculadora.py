import pytest
from calculadora import Calculadora, CalculadoraCientifica

calc = Calculadora()
calc_cient = CalculadoraCientifica()

def test_dividir():
    assert calc.dividir(10, 2) == 5.0

def test_classificar_positivo():
    assert calc.classificar(5) == "positivo"

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calc.dividir(10, 0)

def test_classificar_negativo():
    assert calc.classificar(-3) == "negativo"

def test_classificar_zero():
    assert calc.classificar(0) == "zero"

def test_quadrado():
    assert calc_cient.quadrado(4) == 16

def test_raiz_quadrada():
    assert calc_cient.raiz_quadrada(9) == 3.0

def test_raiz_negativa():
    with pytest.raises(ValueError):
        calc_cient.raiz_quadrada(-1)