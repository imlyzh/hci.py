from typing import Iterable, TypeVar, Generic, Callable

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

del T