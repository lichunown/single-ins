# An Easy-Used Single Instance package (单例模式)

- Support a simple singleton pattern (the created object is globally unique).
- Support implementing the single instance for hashable objects (`__hash__`) (ensure that objects with the same hash value are unique).
- Support implementing the single instance for comparable objects (`__eq__`) (ensure the uniqueness of equal objects).

1. 支持简单的单例模式（创建的对象全局唯一）
2. 支持对可hash的对象，实现单例模式（保证相同hash值的对象唯一）
3. 支持对可比较（`__eq__`）的对象，实现单例模式（保证相等对象的唯一）

## install 

```bash
pip install single-ins
```

## how to use

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
    id_: int

    def __hash__(self):
        return self.id_


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

