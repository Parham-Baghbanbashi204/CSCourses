# doubly linked lists

class DoubleLinkedList:
    class __Node:
        data = None
        previousNode = None
        nextNode = None

        def __init__(self, data, prevNode, nextNode):
            self.data = data
            self.nextNode = nextNode
            self.previousNode = prevNode

        def toString(self):
            return self.__data

    __size = 0
    __head = __Node
    __tail = __Node

    def clear(self):
        pointer = self.__head
        while pointer is not None:
            next_node = pointer.nextNode
            pointer.previousNode = pointer.nextNode = None
            pointer.data = None
            pointer = next_node

    def size(self):
        return self.__size

    def is_emmpty(self):
        return self.size() == 0

    # adding
    def add(self, element):
        self.add_last(element)

    def add_last(self, element):
        if self.is_emmpty():
            self.__head = self.__tail = self.__Node(element, None, None)
        else:
            self.__tail.nextNode = self.__Node(element, self.__tail, None)
            self.__tail = self.__tail.nextNode

        self.__size += 1

    def add_first(self, element):
        if self.is_emmpty():
            self.__head = self.__tail = self.__Node(element, None, None)
        else:
            self.__head.previousNode = self.__Node(element, None, self.__head)
            self.__head = self.__head.previousNode
        self.__size += 1

    # peeking
    def peek_last(self):
        if self.is_emmpty():
            raise RuntimeError("Empty list")
        else:
            return self.__tail.data

    def peek_first(self):
        if self.is_emmpty():
            raise RuntimeError("Empty list")
        else:
            return self.__head.data

    # removals
    def remove_first(self):
        if self.is_emmpty():
            raise RuntimeError("Empty list")
        data = self.__head.data
        self.__head = self.__head.nextNode
        self.__size -= 1

        if self.is_emmpty():
            self.__tail = None
        # memory sweep
        else:
            self.__head.previousNode = None
        return data

    def remove_last(self):
        if self.is_emmpty():
            raise RuntimeError("Empty list")
        data = self.__tail.data
        self.__tail = self.__tail.periviousNode
        self.__size -= 1

        if self.is_emmpty():
            self.__head = None
        else:
            self.__tail.nextNode = None
        return data

    def __remove(self, node):
        node = self.__Node
        if node.previousNode is None:
            return self.remove_first()

        if node.nextNode is None:
            return self.remove_last()

        # make pointers point two ajacent nodes (skip over node)
        node.nextNode.previousNode = node.previousNode
        node.previousNode.nextNode = node.nextNode

        data = node.data
        # memory cleanup
        node = node.previousNode = node.nextNode = None

        self.__size -= 1

        return data

    def remove_at(self, index):
        if index < 0 or index >= self.__size:
            raise ValueError

        if index < self.__size / 2:
            trav = self.__head
            for i in range(index):
                trav = trav.nextNode
        else:
            trav = self.__tail
            i = self.__size
            while i != index:
                trav = trav.previousNode
                i -= 1
        return self.__remove(trav)

    def is_removed(self, object):
        trav = self.__head
        if object is None:
            trav = self.__head
            while trav is not None:
                if trav.data is None:
                    self.__remove(trav)
                    return True
        else:
            trav = self.__head
            while trav is not None:
                if object == trav.data:
                    trav = trav.nextNode
                    self.__remove(trav)
                    return True
        return False

    def index_of(self, obj):
        trav = self.__head
        if obj is None:
            index = 0
            while trav is not None:
                trav = trav.nextNode
                if trav.data is None:
                    return index
                index += 1
        else:
            index = 0
            while trav is not None:
                trav = trav.nextNode
                if obj == trav.data:
                    return index
                index += 1

        return -1

    def list_contains(self, obj):
        return self.index_of(obj) != -1

    def print_list(self):
        output = []
        trav = self.__head
        while trav is not None:
            output.append(trav.data)
            trav = trav.nextNode
        return output


dll = DoubleLinkedList()

dll.add_first(10)
dll.add_last("Hi")
dll.add("sup")
print(dll.peek_first())
print(dll.peek_last())
print(dll.print_list())
