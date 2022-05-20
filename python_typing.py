#!/usr/bin/env python3
from typing import Callable, List, Set, Dict, TypeVar

x = 1
y : int = 1 # y with integer type annotation.
# z : str = 1 # wrong annotation/assignment.
print(x,y)
# print(z)

def abc(a: int, b: int, c: int) -> int:
    return a + b + c

print(abc(11,12,133))

def defi(aa: str, liu: list[str]) -> None:
    print(aa)
    print(liu)

# Old way before 3.8 to annotate complex data types

listy1: List[List[int]] = [[3,4,5],[1,3,4]]
dicty1: Dict[int, str] = {1: "Hola"}
sety1: Set[float] = {3.44}

# New way
listy2: list[list[int]] = [[6,7,55],[1,22]]
dicty2: dict[int, str] = {1: "Hola"}
sety2: set[float] = {673.2}

# Custom type
Vector = list[float]
def some_custom(v: Vector) -> Vector:
    pass 

Vectors = list[Vector]
def some_other_custom(c: Vectors) -> Vector:
    pass

# Optional type
# Below flag is optional boolean parameter
def stuff1(flag: bool = True) -> None:
    pass
stuff1()
# To make it more explicit use Optional
from typing import Optional
def stuff2(flag: Optional[bool] = True) -> None:
    pass
stuff2()

# Any type
from typing import Any
# More explicit way of defining that any type can be assigned to this variable
def any_example(c: Any) -> None:
    pass

# Sequence Type
from typing import Sequence
def seq_example(s: Sequence[str]) -> None:
    pass
seq_example(["1","2","3"])
seq_example(("1","2","3"))
seq_example("hello")
# seq_example({"1","2","3"}) # This won't work because set is not a sequence

# Tuple Type
# We need to define all type of individual tuple elems because it's non mutable
def tup_example(ss: tuple[int, int, int]) -> None:
    pass
tup_example((22,3,3))

# Callable Type
def add(x: int, y: int) -> int:
    return x + y
def call_example(some_func: Callable[[int, int], int]) -> None:
    # Callable[[int, int], int] means
    # It takes a callable has to have two params with int type and returns int
    add(1,333)
call_example(add)

def funcy(x: Optional[int] = 45) -> Optional[int]:
    return x
funcy()
def call_optional_example(funcy: Callable[[Optional[int]], Optional[int]]) -> None:
    funcy(889)
call_optional_example(funcy)

# Generics Type
# Don't know what this T type would be, but i'll call it by name T
T = TypeVar('T')

def get_item(lst: list[T], index: int) -> T:
    return lst[index]