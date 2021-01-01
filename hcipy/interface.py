from typing import Iterable, TypeVar, Generic, Callable
from abc import ABCMeta, abstractmethod
from functools import reduce

T = TypeVar('T')


# '''
# todo...
class Lazy(Generic[T]):

    def __init__(self, clo: Callable[[], T]):
        self.clo: Callable[[], T] = clo

    def __call__(self) -> T:
        return self.clo()
    
    def collect(self) -> T:
        return self()

    R = TypeVar('R')
    def map(self, callable: Callable[[T], R]) -> 'Lazy[R]':
        def r():
            return callable(self())
        return Lazy(r)
# '''

class Iter(Generic[T]):
    v: Iterable[T]

    def __init__(self, v: Iterable[T]):
        self.v = v
    
    def __iter__(self) -> Iterable[T]:
        return self.v.__iter__()

    def filter(self, callable: Callable[[T], bool]) -> 'Iter[T]':
        return Iter(i for i in self.v if callable(i))

    def reduce(self, callable: Callable[[T, T], T]) -> T:
        return reduce(callable, self.v)

    def for_each(self, callable: Callable[[T], None]) -> None:
        for i in self.v:
            callable(i)

    I = TypeVar('I')
    def fold(self, init: I, callable: Callable[[I, T], I]) -> I:
        for i in self.v:
            init = callable(init, i)
        return init

    R = TypeVar('R')
    def map(self, callable: Callable[[T], R]) -> 'Iter[R]':
        return Iter([callable(i) for i in self.v])
    
