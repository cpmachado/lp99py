from typing import Any
from .linked_list import LinkedList


# Exercise 01
def my_last(ll: LinkedList) -> Any:
    if not ll:
        return None

    while ll.next:
        ll = ll.next

    return ll.val
