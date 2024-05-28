from single_ins import SingleInstance


class Foo(SingleInstance):

    def __init__(self):
        pass


if __name__ == '__main__':
    assert id(Foo()) == id(Foo())

