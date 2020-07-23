# doubly linked lists

class DoubleLinkedList:
    __size = 0
    __head = None
    __tail = None

    class __Node:
        __data = None
        __previousNode = None
        __nextNode = None
        def __init__(self, data, prevNode, nextNode):
            self.__data = data


