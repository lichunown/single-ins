from single_ins import SingleHashableInstance
from dataclasses import dataclass


class Foo(SingleHashableInstance):

    def __init__(self, v):
        self.v = v

    def __hash__(self):
        return self.v


@dataclass
class Data(SingleHashableInstance):
    v: int

    def __hash__(self):
        return self.v


if __name__ == '__main__':
    assert id(Foo(1)) == id(Foo(1))
    assert id(Foo(2)) != id(Foo(1))

    assert id(Data(1)) == id(Data(1))
    assert id(Data(2)) != id(Data(1))
