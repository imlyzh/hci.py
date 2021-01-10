from typing import TypeVar, Generic, Callable, Tuple, Iterable
from .iter import Iter

P = TypeVar('P')
R = TypeVar('R')

class Func(Generic[P, R]):
    v: Tuple[Callable[[P], R]]

    def __init__(self, v: Callable[[P], R]):
        self.v = (v,)
    
    def __call__(self, p: P) -> R:
        return self.v[0](p)
    
    def __mod__(self, p: P) -> R:
        return self(p)
    
    R1 = TypeVar('R1')
    def __or__(self, callable: Callable[[R], R1]) -> 'Func[P, R1]':
        return Func(lambda p: callable(self(p)))
    
    def __ror__(self, other: Iterable[P]) -> 'Iter[R]':
        return Iter([self(i) for i in other])
    
    def __rshift__(self, callable: Callable[[R], R1]) -> 'Func[P, R1]':
        return self | callable
    
    P1 = TypeVar('P1')
    def __lshift__(self, callable: Callable[[P1], P]) -> 'Func[P1, R]':
        return Func(lambda p: self(callable(p)))

    def pipe(self, callable: Callable[[R], R1]) -> 'Func[P, R1]':
        return self | callable
    
    def apply(self, p: P) -> R:
        return self % p

del P, R

T = TypeVar('T')
def identity(id: T) -> T:
    return id

del T