"""
Es un objeto invocable simple sin la declaracion def
Ni siquiera es necesario que el objeto invocable se vincule a una variable
si lo pasamos directamente a una funcion.

Lambda es una expresion que da como resultado un objeto invocable.
Podemos vincular el resultado de la expresion lambda a una variable
mediante asignacion. El objeto resultante es una funcion, no tiene un
nombre y es invocable como una funcion.

No tiene sentencia return

El uso excesivo de lambdas puede servir para confundir en lugar de aclarar
el codigo cuando se encuentra con los principios pitonicos que valoran
la legibilidad tan altamente.
"""


def _ej1():
    a = lambda: 'a'
    print(a, a())  # <function LambdaExamples._ej1.<locals>.<lambda> at 0x7fed71310d08>, a


def _ej2():
    b = lambda letter: letter.upper()
    print(b, b('a'))  # <function LambdaExamples._ej2.<locals>.<lambda> at 0x7f7d37567d08>, A

    var = 5
    print((lambda: 1 + var)())  # 6, invocamos directamente la lambda como una funcion


def _ej3():
    b = lambda a1, a2, a3: a1 + a2 + a3
    print(b, b(3, 3, 3))  # <function LambdaExamples._ej3.<locals>.<lambda> at 0x7fb97cd67d08> 9


def _map_example():
    # map: apply a function to every element in a sequence. Retorna un iterador que luego hay que iterarlo.
    # producing a new sequence. Ejemplo: map(function, iterable, ...)

    numbers = (2, 2, 2, 2)
    result = map(lambda n: n*n, numbers)
    print(type(result))  # <class 'map'>
    #print(next(result), next(result), next(result), next(result))
    print('Iterando el map: ', [n for n in result])
    print('Iterando el map: ', list(result))

    def calculate_square(n):
        return n*n

    result = map(calculate_square, numbers)  # invoca la funcion calculate_square()
    print(next(result), next(result), next(result), next(result))

    num1 = [4, 5, 6]
    num2 = [5, 6, 7]
    result = map(lambda n1, n2: n1 + n2, num1, num2)
    print(list(result))

    # number_list = range(-5, 5)
    # less_than_zero = list(filter(lambda x: x < 0, number_list))


def _filter_example():
    """
    filter: filtra los elementos de una secuencia a traves de una condicion,
    produciendo una nueva secuencia. Retorna una lista de los elementos filtrados.
    """
    positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])  # <class 'filter'>
    print(list(positives))  # [1, 6, 8] de convertirlo en una lista para iterarlo


if __name__ == '__main__':
    _filter_example()
