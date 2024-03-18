"""
funciones o invocables, que pueden aceptar argumentos posicionales o de
palabras clave arbitrarios.

https://app.pluralsight.com/course-player?clipId=12ff0f3e-99f7-4246-9a7b-c2f30fd549e0
https://app.pluralsight.com/library/courses/python-beyond-basics/table-of-contents

Respetar el orden de los argumentos en las firmas de los metodos:
Si la firma va a contener:
    **kwars y *args, **kwars debe preceder de *args. Ejemplos: def fun(*args, **kwargs): pass

    **kwargs y arg2(argumento posicional), **kwargs debe preceder de arg2. Ejemplos: def fun(arg2, **kwargs): pass

    *args y arg2, el orden se puede cambiar, no da error. Ejemplos def fun(*args, arg2): pass | def fun(arg, *args): pass

    arg1, arg2, *args3, arg4, arg5, *args6, este da error luego de un argumento
    variable puede ir un posicional y luego de ese posicional no puede ir otro argumento variable,
    cuando declaramos el metodo no da error de sintaxis pero si da error de sintaxis cuando
    invocamos el metodo asignandole valores.

    OK
    arg1, arg2, *args3, arg4, arg5, **args6
    *args1, arg2, **args3

    ERROR
    *args1, arg2, *args3
    **kwars, *args
    **kwargs, arg2
    **arg1, arg2, *arg3
"""


def args1(*args):
    print(args)


def kwargs1(**kwargs):
    print(kwargs)  # {'key1': 1, 'key2': 2, 'key3': 3}


def args_kwargs(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    #args1(1)  # (1,)
    #args1(1, 2, 3, 4)  # (1, 2, 3, 4)
    #args1([1, 2, 3, 4])  # ([1, 2, 3, 4],) la lista ingresa como un elemento de la tupla
    #kwargs1(key1=1, key2=2, key3=3)

    #args_kwargs([1, 2, 3])  # (1, 2, 3) {}
    #args_kwargs([1, 2, 3], key1=1, key2=2, key3=3)  # ([1, 2, 3],) {'key1': 1, 'key2': 2, 'key3': 3}

    # args_kwargs(key1=1, key2=2, key3=3)  # () {'key1': 1, 'key2': 2, 'key3': 3}

    args_kwargs()  # () {}


