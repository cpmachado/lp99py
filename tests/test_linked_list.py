from lp99py.linked_list import LinkedList, list_to_linked_list


def test_list_to_linked_list():
    a = ['a', 'b', 'c', 'd', 'e']
    la = list_to_linked_list(a)

    assert isinstance(la, LinkedList)

    # use list compreension to check iterator as well
    assert [x for x in la] == a
