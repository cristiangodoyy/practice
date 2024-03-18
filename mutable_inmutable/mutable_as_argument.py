
def arg_as_default1():
    def arg_as_default_inner(li=[]):
        """
        Es funcion no va a crear una lista li vacia cada vez que la invocamos.
        Se usa la misma lista cada vez que invocamos la funcion.

        Cuando	fijamos	el valor de	un argumento en una funcion es conveniente
        tener en cuenta que este deberia ser de tipo inmutable. En caso
        contrario podriamos obtener resultados inesperados, si el objeto es mutable.
        No se debe emplear objetos como listas, diccionarios o
        instancias de clase	con argumentos por defecto en una funcion.
        """
        li.append(1)
        li.append(2)
        li.append(3)
        print(li)

        """
        En lugar de devolver una lista con un unico valor,
        dado que la lista es inicializada en el argumento por defecto,
        Python devuelve la misma lista con un nuevo valor cada vez que la
        funcion es invocada.

        Esto se debe a que el interprete crea los
        valores por defecto cuando la sentencia que define la funcion es
        ejecutada, def. Cuando se carga el archivo lo primero que se hace es
        inicializar los parametros de las funciones de las clases
        y no cuando la funcion es invocada, cuando la funcion es invocada
        se omiten los valores por defecto con elementos mutables.

        Sin embargo, ¿porque el	comportamiento	de nuestro parametro x
        es diferente? Simplemente porque x es inmutable, mientras
        que li es mutable. La lista puede cambiar su
        valor, que	es precisamente lo que hace nuestra función de
        ejemplo, añadiendo un nuevo	elemento cada vez que la misma es invocada.
        """

    arg_as_default_inner()
    arg_as_default_inner()
    arg_as_default_inner()
    arg_as_default_inner()
    """
    las invocaciones anteriores van a usar la misma lista cada vez que invocamos la funcion
    [1, 2, 3]
    [1, 2, 3, 1, 2, 3]
    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    """


def arg_as_default1_ok():
    def arg_as_default_inner_ok(li=None):
        """
        Si quiero obtener una lista vacia cada vez que invoco la funcion arg_as_default_inner_ok
        """
        if li is None:
            li = []
        li.append(1)
        li.append(2)
        li.append(3)

        print(li)

    arg_as_default_inner_ok()
    arg_as_default_inner_ok()
    arg_as_default_inner_ok()


if __name__ == '__main__':
    #arg_as_default1()
    arg_as_default1_ok()
