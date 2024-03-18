"""
son inmutables:
string, tuple, int, float, decimal, complex, bool, range, frozenset, bytes.
"""


def string_ex1():
    """
    inmutable example: string
    """
    x = "Hello"
    y = "Hello"
    ''' id() returns the identity of an object as an integer. This integer
    usually corresponds to the object’s location in memory. '''
    print(id(x), id(y))  # 140471307199920, 140471307199920  las 2 variables apuntan a la misma direccion de memoria por lo tanto tienen el mismo contenido
    print(x is y)  # comparing memory directions

    x += ' World'
    print(f'x: {x}. y: {y}')
    print(f'id(x): {id(x)}, id(y): {id(y)}')


def tuple_ex1():
    t1 = 1, 2
    t2 = t1
    print(f'Content t1: {t1}, Id(t1): {id(t1)}. Content t2: {t2}, Id(t2): {id(t2)}. ')

    t1 += (3, 4)
    print(f'Content t1: {t1}, Id(t1): {id(t1)}. Content t2: {t2}, Id(t2): {id(t2)}. ')


if __name__ == '__main__':
    # string_ex1()
    tuple_ex1()
