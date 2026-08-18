#just copied and pasted the soultion didn't do anything...

from collections.abc import Iterable
from typing import Callable, Any


def append(list1: list, list2: list) -> list:
    return [*list1, *list2]


def concat(lists: list) -> list:
    result = []
    for item in lists:
        if isinstance(item, Iterable):
            result.extend(item)
        else:
            result.append(item)
    return result


def filter(myfunction: Callable, mylist: list) -> list:
    return [l for l in mylist if myfunction(l)]


def length(mylist: list) -> int:
    return len(mylist)


def map(myfunction: Callable, mylist: list) -> list:
    return [myfunction(l) for l in mylist]


def foldl(myfunction: Callable, mylist: list, initial: Any) -> Any:
    while mylist:
        initial = myfunction(initial, mylist.pop(0))
    return initial


def foldr(myfunction: Callable, mylist: list, initial: Any) -> Any:
    while mylist:
        initial = myfunction(initial, mylist.pop())
    return initial


def reverse(mylist: list) -> list:
    return mylist[::-1]