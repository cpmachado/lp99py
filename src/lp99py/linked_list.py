from dataclasses import dataclass
from functools import reduce
from typing import Any, Callable, TypeVar


LinkedListType = TypeVar("LinkedListType", bound="LinkedList")


class LinkedListIterator:
    def __init__(self, iterated_list: LinkedListType):
        self.iterated_list = iterated_list

    def __next__(self):
        if self.iterated_list:
            val = self.iterated_list.val
            self.iterated_list = self.iterated_list.next
            return val
        raise StopIteration


@dataclass
class LinkedList:
    val: Any
    next: LinkedListType | None

    def __iter__(self):
        return LinkedListIterator(self)


def list_to_linked_list(anyList: list[Any]) -> LinkedList:

    f: Callable[[LinkedList, LinkedList], LinkedList] = \
        (lambda acc, curr: LinkedList(curr, acc))

    return reduce(f, reversed(anyList), None)
