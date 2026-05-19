class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero!")
        return a / b

    def classificar(self, n):
        if n > 0:
            return "positivo"
        elif n < 0:
            return "negativo"
        else:
            return "zero"

    def somar_lista(self, lista):
        total = 0
        for n in lista:
            total += n
        return total

    def contar(self, n):  # pragma: no cover
        while n > 0:
            n -= 1
        return n


class CalculadoraCientifica(Calculadora):
    def quadrado(self, n):
        return n ** 2

    def raiz_quadrada(self, n):
        if n < 0:
            raise ValueError("Número negativo!")
        return n ** 0.5