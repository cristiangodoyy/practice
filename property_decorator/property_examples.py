"""
@Properties
    Getter
    getter se declara con el decorador @property
    setter se declara con @nombre_getter.setter
    se usa para hacer funcionar un metodo como una propiedad
    si una propiedad es calculada usar un @property

    util cuando los atributos(variables de instancia) requieren de un
    procesamiento inicial en el momento de ser accedidos.

    @property el decorador se usa solo para el metodo getter.
    def area(self): pass

    Setter
    @area.setter  # metodo setter. El nombre del setter debe ser igual al nombre del getter.
    def area(self, valor):  # el setter debe recibir valor para asignar.
        self.radio = valor
        # return self.radio # el setter no debe retornar nada.
"""


def property_example_1():

    class Circle:
        PI = 3.1415

        def __init__(self, radio):
            self.radio = radio

        @property
        def area(self):  # metodo getter
            """
            La firma debe ser sin argumentos solo incluir self.
            El getter solo debe tener el decorador @property
            """
            return Circle.PI * (self.radio ** 2)

        @area.setter
        def area(self, valor):
            """
            el setter debe tener el decorador @metodo_getter.setter
            para el setter asigno el valor asi:
            ci = Circle(4)
            ci.area = 5
            """
            self.radio = valor
            # return self.radio # el setter no debe retornar nada.

    ci = Circle(4)
    # print(f'Radio: {ci.radio}, Area: {ci.area}')
    ci.area = 5  # setter: @area.setter
    print(type(ci.area))  # getter: @property
    print(ci.area)


def property_practice():
    class Circle:
        PI = 3.1415

        def __init__(self, radio):
            self.radio = radio

        @property
        def area(self):
            return Circle.PI * (self.radio ** 2)

        @area.setter
        def area(self, value):
            self.radio = value

    ci = Circle(3)
    print(ci.area)

    ci.area = 5

    print(ci.area)


if __name__ == "__main__":
    # property_example_1()
    property_practice()
