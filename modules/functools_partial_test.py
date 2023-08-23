from functools import partial
from itertools import repeat


def do_repeat(element: object, number_of_repeat: int):
    return repeat(element, number_of_repeat)

hello = partial(do_repeat, 'Hello!!!')

print(list(hello(5)))