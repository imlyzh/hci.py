from typing import TypeVar, Generic, Callable


T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')
T6 = TypeVar('T6')
T7 = TypeVar('T7')
T8 = TypeVar('T8')
T9 = TypeVar('T9')
T10 = TypeVar('T10')
T11 = TypeVar('T11')
T12 = TypeVar('T12')
T13 = TypeVar('T13')
T14 = TypeVar('T14')
T15 = TypeVar('T15')
T16 = TypeVar('T16')
R = TypeVar('R')

class Func0(Generic[R]):
    callable: Callable[[], R]

class Func1(Generic[T1, R]):
    callable: Callable[[T1], R]

class Func2(Generic[T1, T2, R]):
    callable: Callable[[T1, T2], R]

class Func3(Generic[T1, T2, T3, R]):
    callable: Callable[[T1, T2, T3], R]

class Func4(Generic[T1, T2, T3, T4, R]):
    callable: Callable[[T1, T2, T3, T4], R]