class A:
    def __init__(self, attra1, attra2):
        self.attra1 = attra1
        self.attra2 = attra2


class B(A):
    def __init__(self, attrb1, attrb2, attra1, attra2):
        #super().__init__(attra1, attra2)
        super().__init__(attra1, attra2)
        self.attrb1 = attrb1
        self.attrb2 = attrb2


class B2(A):
    def __init__(self, attrb1, attrb2, *args):
        """
        Con argumentos variables
        Para esta version con *args la unica forma de instanciar es sin especificar
        argumentos posicionales b2 = B2(1, 2, 3, 4)
        los argumentos quedan asi:
        attrb1=1, attrb2=2, *args=(3, 4)
        """
        # son las 3 formas de invocar a super para asignar los valores
        # a las variables de la clase que se hereda
        super().__init__(*args)
        #super(B2, self).__init__(args[0], args[1])
        #super(B2, self).__init__(attra1=args[0], attra2=args[1])

        self.attrb1 = attrb1
        self.attrb2 = attrb2


class B3(A):
    def __init__(self, attrb1, attrb2, **kwargs):
        """
        Para esta version con *args la unica forma de instanciar es sin especificar
        argumentos posicionales  b3 = B3(1, 2, attra1=3, attra2=4)
        los argumentos quedan asi:
        attrb1=1, attrb2=2, kwargs={'attra1': 3, 'attra2': 4}
        """
        super().__init__(**kwargs)
        # super(B3, self).__init__(kwargs['attra1'], kwargs['attra2'])
        # super().__init__(attra1=kwargs['attra1'], attra2=kwargs['attra2'])
        self.attrb1 = attrb1
        self.attrb2 = attrb2


class C(A):
    def __init__(self, attrc1, *args):
        #super().__init__(attra1, attra2)
        super(C, self).__init__(*args)
        self.attrc1 = attrc1


if __name__ == '__main__':
    # b = B(attrb1=1, attrb2=2, attra1=3, attra2=4)
    # print(b.__dict__)

    # b2 = B2(1, 2, 3, 4)
    # print(b2.__dict__)

    b3 = B3(1, 2, attra1=3, attra2=4)
    #b3 = B3(attrb1=1, attrb2=2, attra1=3, attra2=4)
    print(b3.__dict__)
