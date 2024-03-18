"""
Para crear un decorador tener en cuenta lo siguiente:
Funcion decoradora:
    Recibe(la funcion que va a decorar) un objeto invocable como argumento, es decir una funcion f.
    Contiene dentro una funcion(wrap) que envuelve a la funcion(decorada) que ingreso como argumento.
    Retorna un invocable, es decir a la funcion que envulve(wrap): return wrap

Funcion que envuelve(wrap)
    Recibe los parametros wrap(*args, **kwargs) de la funcion decorada f si es necesario.
    Invoca a la funcion decorada y con argumentos(*args, **kwargs) si es necesario.
    Puede tener codigo antes y despues de invocar a la funcion decorada para agregar
    funcionaminto.
    Si es necesario puede obtener el valor de la funcion f decorada y hacer algo con
    el valor.

Funcion decorada (f):
    Ingresa como Argumento en el decorador
    Se debe invocar con su nombre y parentisis dentro de la funcion que envuelve(wrap).
    Debemos agregar codigo antes y despues de que invocamos la funcion f decorada para establecer
    comportamiento. Si recibe parametros declarar *args y **kwargs para recibirlos.
    Si retorna valor, obtener el valor de retorno para hacer algo con su valor si es necesario.
    Luego si se hizo algo con el valor que obtuvo de la funcion decorada debe retornar el
    el nuevo valor con un return: return uppercase(value)
"""


def example_decorator_1():

    def convert_lower(f):
        def wrap(arg):  # f receive only one argument
            result = f(arg)  # f receive only one argument
            return result.lower()
        return wrap

    @convert_lower
    def decorated(word):
        return word

    print(decorated('ARGENTINA'))


def example_decorator_2():
    def convert_lower(f):
        def wrap(arg1, arg2, arg3):  # f receive only one argument
            result = f(arg1, arg2, arg3)  # f receive only one argument
            return result.lower()
        return wrap

    @convert_lower
    def decorated(word1, word2, word3):
        return word1 + word2 + word3

    print(decorated('HELLO', ', ', 'WORLD'))


def example_decorator_3():
    def convert_lower(f):
        def wrap(*args):  # f receive only one argument
            result = f(*args)  # f receive only one argument
            return result.lower()
        return wrap

    @convert_lower
    def decorated(*args):
        return args[0] + args[1] + args[2]

    print(decorated('HELLO', ', ', 'WORLD'))


def example_decorator_4():
    def convert_lower(f):
        def wrap(*args):  # receive three arguments in a tuple
            result = f(*args)
            return result.lower()
        return wrap

    @convert_lower
    def decorated(*args, **kwargs):
        print(args[0] + args[1] + args[2])

    print(decorated('HELLO', ', ', 'WORLD'))


def decorator_practice():
    def decorator(f):
        def wrap(*args):  # args incoming as tuple ('HELLO', ', ', 'WORLD')
            result = f(*args)
            return result.lower()
        return wrap

    @decorator
    def decorated(*args):  # args incoming as tuple ('HELLO', ', ', 'WORLD')
        return args[0] + args[1] + args[2]

    print(decorated('HELLO', ', ', 'WORLD'))


if __name__ == '__main__':
    # example_decorator_1()
    example_decorator_2()
    # example_decorator_3()
    # decorator_practice()
