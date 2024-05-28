from single_ins import SingleEqualableInstance


class Foo(SingleEqualableInstance):

    def __init__(self, v, b=1, *args, **kwargs):
        self.v = v

    def __eq__(self, other):
        if not isinstance(other, Foo):
            return False
        return self.v == other.v


if __name__ == '__main__':
    assert id(Foo(1)) == id(Foo(1))
    assert id(Foo(2)) != id(Foo(1))
