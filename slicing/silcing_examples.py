"""
Example 1.18. Slicing shorthand
-------------------------------
(1) If the left slice index is 0, you can leave it out, and 0 is implied. So li[:3] is the same as li[0:3]
from the previous example.

(2) Similarly, if the right slice index is the length of the list, you can leave it out. So li[3:] is the same as
li[3:5], because this list has 5 elements.

(3) Note the symmetry here. In this 5−element list, li[:3] returns the first 3 elements, and li[3:] returns
the last 2 elements. In fact, li[:n] will always return the first n elements, and li[n:] will return the
rest, regardless(independientemente) of the length of the list.

(4) If both slice indices are left out, all elements of the list are included. But this is not the same as the
original li list; it is a new list that happens to have all the same elements. li[:] is a shorthand for
making a complete copy of a list.
"""


class Slicing:

    @classmethod
    def list_1(cls):
        li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # all elements
        print(f'List print all elements: {li[:]}')

        # first element
        print(f'Print first element version 1: {li[0]}')
        print(f'Print first element version 2: {li[-9]}')

        # last element
        print(f'Print last element version 1: {li[-1]}')
        print(f'Print last element version 1: {li[9]}')
        print(f'Print last element version 3: {li[len(li) - 1]}')

        # get a sublist
        print(f'Print sublist [3, 4, 5, 6]: {li[2:6]}')
        print(f'Print sublist [8, 9, 10]: {li[-3:]}')

        # slicing with saltos
        print(f'Print sublist [1, 3, 5, 7, 9]: {li[0:10:2]}')

    @classmethod
    def tuple_1(cls):
        li = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # all elements
        print(f'List print all elements: {li[:]}')

        # first element
        print(f'Print first element version 1: {li[0]}')
        print(f'Print first element version 2: {li[-9]}')

        # last element
        print(f'Print last element version 1: {li[-1]}')
        print(f'Print last element version 1: {li[9]}')
        print(f'Print last element version 3: {li[len(li) - 1]}')

        # get a sublist
        print(f'Print subtuple [3, 4, 5, 6]: {li[2:6]}')
        print(f'Print subtuple [8, 9, 10]: {li[-3:]}')

        # slicing with saltos
        print(f'Print subtuple [1, 3, 5, 7, 9]: {li[0:10:2]}')


if __name__ == '__main__':
    # Slicing.list_1()
    Slicing.tuple_1()
