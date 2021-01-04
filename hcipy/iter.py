from typing import Iterable, TypeVar, Generic, Callable, Dict, Tuple, List, Set
from functools import reduce

T = TypeVar('T')

class Iter(Generic[T]):
    v: Iterable[T]

    def __init__(self, v: Iterable[T]):
        self.v = v
    
    def __iter__(self) -> Iterable[T]:
        return self.iter()

    R = TypeVar('R')
    def __or__(self, callable: Callable[[T], R]) -> 'Iter[R]':
        return Iter([callable(i) for i in self.v])
    
    def iter(self) -> Iterable[T]:
        return self.v.__iter__()
    
    def list(self) -> List[T]:
        return list(self.iter())

    def set(self) -> Set[T]:
        return set(self.iter())

    def filter(self, callable: Callable[[T], bool]) -> 'Iter[T]':
        return Iter(i for i in self.v if callable(i))

    def reduce(self, callable: Callable[[T, T], T]) -> T:
        return reduce(callable, self.v)

    def map(self, callable: Callable[[T], R]) -> 'Iter[R]':
        return self | callable

    def for_each(self, callable: Callable[[T], None]) -> None:
        for i in self.v:
            callable(i)
    
    def apply(self, callable: Callable[[Iterable[T]], Iterable[R]]) -> 'Iter[R]':
        return Iter(callable(self.iter()))

    I = TypeVar('I')
    def fold(self, init: I, callable: Callable[[I, T], I]) -> I:
        for i in self.v:
            init = callable(init, i)
        return init
    
    KT = TypeVar('KT')
    VT = TypeVar('VT')

    @staticmethod
    def from_dict(i: Dict[KT, VT]) -> 'Iter[Tuple[KT, VT]]':
        return Iter(i.items().__iter__())
    
    @staticmethod
    def into_dict(i: 'Iter[Tuple[KT, VT]]') -> Dict[KT, VT]:
        return { p[0]: p[1] for p in i.iter() }


del T
