

def list_mutable1():
    a = [1, 2, 3]
    b = a

    print(a, b)

    b.append(99)

    print(f'id a: {id(a)} content a: {a}.  id b: {id(b)} content b: {b}')


def list_mutable_distinct_dir_memory_but_same_content():
    a = [1, 2, 3]
    b = [1, 2, 3]

    print(f'Distinct dir of memory but same content. id a: {id(a)} content a: {a}.  id b: {id(b)} content b: {b}')


def dict_mutable_1():
    a = {'k1': 'val1', 'k2': 2}
    b = a

    print(id(a), id(b))

    b['k3'] = [1, 2, 3]

    print(a, b)


if __name__ == '__main__':
    #list_mutable1()
    # list_mutable_distinct_dir_memory_but_same_content()
    dict_mutable_1()