from lp99py.linked_list import list_to_linked_list
from lp99py.lists import my_last


# Exercise 01
def test_my_last():
    def none_test():
        assert my_last(None) is None

    def main():
        la = list_to_linked_list(['a', 'b', 'c', 'd'])

        assert my_last(la) == 'd'

    def break_heap():
        la = list_to_linked_list([x for x in range(2048)])

        assert my_last(la) == 2047

    none_test()
    main()
    break_heap()
