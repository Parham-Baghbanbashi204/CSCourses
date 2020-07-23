from DataStructuresPython import linkedLists


class Stack(object):
    list = linkedLists.DoubleLinkedList()

    def push(self, elem):
        self.list.add(elem)

    def size(self):
        return self.list.size()

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            raise ValueError("empty stack")
        self.list.remove_last()

    def peek(self):
        if self.is_empty():
            raise ValueError("Empty Stack")
        return self.list.peek_last()


'''
stack = Stack()
stack.push(10)
stack.push("Howdy")
stack.push("Ma'am")
stack.push("How are you")
print(stack.peek())
'''
