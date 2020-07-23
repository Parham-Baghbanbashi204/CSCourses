arr = []

# apend to array

arr.append(1)

# insert element at given index
arr.insert(0, "hi")

list2 = ["hellow there"]

# adds two lists together
arr.extend(list2)

# remove items from an array
arr.remove("hi")

# sorts an array
arr.sort()

# reverses the list in place (does not return it)
arr.reverse()

# removes and returns the element at the given index.
# Returns the rightmost element if index is omitted 
# (roughly the opposite of append()).
arr.pop(1)


class Array():
    # use def __init__(self, *args) to pass as meany arguments you want
    # and use **kwargs to parse variables
    # __ is private

    def __init__(self, capacity_value):
        self.arr = []
        self.len = 0
        self.capacity = 0
        if (capacity_value < 0):
            raise ValueError("Illigal capacity", capacity_value)
        self.capacity = capacity_value
        self.arr = [0 for i in range(capacity_value)]

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def get(self, index):
        return self.arr[index]

    def set(self, index, element_value):
        self.arr[index] = element_value

    def clear(self):
        for i in range(len(arr)):
            arr.pop(i)

    def add(self, elem):
        ''' java way
        if(len+1 >= self.capacity):
            self.capacity = 1
        else:
            self.capacity *= 2
        new_arr = [for i in range(self.capacity)]
        for i in range(len):
            new_arr[i] = self.arr[i]
            self.arr = new_arr
        arr[len+1] = elem
        '''
        # python way
        self.arr.append(elem)

    def removeAt(self, rm_index):
        self.capacity = -len(rm_index)
        return self.arr.pop(rm_index)

    def remove(self, elem):
        self.arr.remove(elem)

    def indexOf(self, elem):
        for i in range(len(self.arr)):
            if (self.arr[i] == elem):
                return i
        return -1

    def contain(self, element):
        return self.indexOf(element) != -1
