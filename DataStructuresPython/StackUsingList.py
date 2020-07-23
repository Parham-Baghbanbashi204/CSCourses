# same as stackOOP just is using a list insted
# lists in python are everything from arrays
# to doubly linked lists to stacks but this takes 0(n) compared to dque
stack = []

# same as stackOOP.push
print("Pusing to stack")
stack.append(10)
stack.append("Howdy")
stack.append("Ma'am")
stack.append("how are you")
stack.append("end")
# full stack
print(stack)

print('\nPoping elements from stack')
# use list.pop to pop element form stack in LIFO order
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
