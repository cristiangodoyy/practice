def list_for_comprehension_1():
    """
    Generar el siguiente codigo con comprension de listas
    cuadrados = []
    for i in range(5):
        cuadrados.append((i, i+1))  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
    """
    li = [(i, i*i) for i in range(5)]
    print(li)


def list_for_comprehension_2():
    """
    Convertir a list for comprehension
    result = []
    for x in range(10):
        for y in range(x):
            result.append((x, y))
    """

    result = [(x, y) for x in range(10) for y in range(x)]  # list as comprehensions
    print(type(result))
    print(result)


def list_for_comprehension_3():
    """
    Convertir con list for comprehension
    values = []
    for x in range(4):
        if x > 2:
            for y in range(4):
                if x - y != 0:
                    values.append(x / (x - y))
    print(values)
    """
    # can use multiple input sequences and multiple if-clauses

    values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
    print(values)

    values = [x / (x - y)
              for x in range(100)
              if x > 50
              for y in range(100)
              if x - y != 0]
    print(values)


def list_for_comprehension_practice():
    """
    outer = []
    for x in range(10):
        inner = []
        for y in range(x):
            inner.append(y * 3)
        outer.append(inner)
    """
    pass


def dict_for_comprehension_1():
    """
    Mostrar el siguiente diccionario con comprension de diccionarios:
    {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    dic = {}
    for i in range(5):
        dic[i] = i+1
    print(dic)
    """
    dic = {i: i+1 for i in range(5)}
    print(dic)


def dict_for_comprehension_2():
    set1 = {x for x in range(10)}  # dict as comprehensions
    print(type(set1))
    print(set1)

    set2 = (x for x in range(10))  # It creates a generator
    print(type(set2))
    for x in set2:
        print(x)


def dict_for_comprehension_practice():
    dic = {}
    for i in range(5):
        dic[i] = i+1
    print(dic)


def dict_for_comprehension_3():
    """
    dic = {}
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                dic[x] = y
    """
    l1 = [1, 2, 3]
    l2 = [3, 1, 4]

    di = {x: y for x in l1 for y in l2 if x != y}
    print(di)


def comprehension_practice():
    """
    1.
    Generar el siguiente codigo con comprension de listas
    cuadrados = []
    for i in range(5):
        cuadrados.append((i, i+1))  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
    """

    """
    Convertir a list for comprehension
    result = []
    for x in range(10):
        for y in range(x):
            result.append((x, y))
            
    la salida es la siguiente: [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
    """


    """
    Convertir con list for comprehension
    values = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x - y != 0:
                    values.append(x / (x - y))
    print(values)  [1.0, 1.5, 3.0]
    """
    #print([x / (x - y) for x in range(4) if x > 2 for y in range(4) if x - y != 0])

    """
    Mostrar el siguiente diccionario con comprension de diccionarios:
    {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}

    dic = {}
    for i in range(5):
        dic[i] = i+1
    print(dic)
    """
    # print({x: x+1 for x in range(5)})

    """
    dic = {}
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                dic[x] = y
    print({1: 4, 2: 4, 3: 4})
    """
    print({x: y for x in [1, 2, 3] for y in [3, 1, 4] if x != y})


if __name__ == '__main__':
    #list_for_comprehension_1()
    #list_for_comprehension_2()
    #list_for_comprehension_3()
    #dict_for_comprehension_1()
    #dict_for_comprehension_2()
    #dict_for_comprehension_3()
    comprehension_practice()
