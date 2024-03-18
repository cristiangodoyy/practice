def gen_as_function():
    """
    Un metodo que recibe una cantidad(la cantiad de veces que se tiene que iterar el iterable)
    y un iterable.
    Itero sobre los items del iterable:
        - Si ya se itero la cantidad de veces ingresada salgo del metodo
        - De lo contrario retorno el valor
    """
    def gen_fun(count, iterable):
        counter = 0

        for item in iterable:
            if counter == count:
                return
            counter += 1
            yield item
        print('Exit')  # never print this line

    my_gen = gen_fun(3, [1, 2, 3, 4, 5, 6])

    for item in my_gen:
        print(item)


def generator_as_expression():
    """
    Calculate a square of the first 4 integers numbers
    """
    gen_express = (x*x for x in range(5))

    for item in gen_express:
        print(item)


def generator_practice():
    """
    Un metodo que recibe una cantidad(la cantiad de veces que se tiene que iterar el iterable)
    y un iterable.
    Itero sobre los items del iterable:
        - Si ya se itero la cantidad de veces ingresada salgo del metodo
        - De lo contrario retorno el valor
    """
    def gen_fun(count, iterable):
        counter = 0

        for item in iterable:
            if counter == count:
                return
            counter += 1
            yield item
        print('Exit')

    gen = gen_fun(3, [1,2,3,4,5,6,7,8,9])

    for item in gen:
        print(item)


if __name__ == "__main__":
    # gen_as_function()
    #generator_as_expression()
    generator_practice()
