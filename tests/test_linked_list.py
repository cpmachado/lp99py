from lp99py.linked_list import LinkedList, listToLinkedList


def test_listToLinkedList():
    a = ['a', 'b', 'c', 'd', 'e']
    la = listToLinkedList(a)

    assert isinstance(la, LinkedList)

    # use list compreension to check iterator as well
    assert [x for x in la] == a
