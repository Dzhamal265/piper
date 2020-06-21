from functools import partial

from piper import pipe


def test_pipe():
    def pow(a, b):
        return a ** b

    power = partial(pow, b=2)
    funcs = (max, lambda x: [1] * x, sum, power)
    assert pipe(*funcs)([1, 2, 100, 3, 4]) == 10000
