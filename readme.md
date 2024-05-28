# An Easy-Used Single Instance package

- support simple single instance
- support 

## install 

```bash
pip install single-ins
```

## how to use

### SingleHashableInstance

```python
from single_ins.hashable_si import SingleHashableInstance
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
```

### SingleEqualableInstance

```python
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

```

### SingleInstance

```python

from single_ins import SingleInstance


class Foo(SingleInstance):

    def __init__(self):
        pass


if __name__ == '__main__':
    assert id(Foo()) == id(Foo())
    assert id(Foo.instance) == id(Foo())
```