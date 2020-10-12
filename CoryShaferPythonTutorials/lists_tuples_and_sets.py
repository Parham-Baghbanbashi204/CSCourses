# Lists 
# creating a list
courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Course']
#functions
    # len --> prints the length of the list
    # courses[0] --> indexing
    # append --> adds stuff to the list
    # insert(index, list) --> Inserts one list to another ex: courses.insert(0, courses2) --> inserts courses two at index zero of courses:  
    # extend(list_to_add) -- like append but with lists: Ex: courses.extend(courses2) --> appends all the items in courses 2 to courses: big diffrence is that append wil just add the list as the last index
    # extend appends the list CONTENTS  
    # removing items:
    # remove(item) --> removes the item
    # pop(index) -- removes the last value of the list if no index is given: lets us use a list like a stack or a queue
    # reverse --> reverses the order of the list
    # sort() --> sorts the list in alpahetical or accending order --> takes argurment reverse: reverse the sort order
    # sorted(itrable) --> retuns a sorted verson of the list --> does not touch the list
    # min, max, and sum, --> self evedent: takes itrable
    # index(item) --> gets the index of the items 
    # in(item) --> returns true or false if the item is in the list: ex: print('art' in courses) --> Returns False
    # enumerate(itrable) --> returns both the index and value of an item in the itrable --> takes a start valuble
    # str.join(list) --> joins the items of that list to the string
    # str.split(seperator) --> splits the string by it seperator ex
new_courses = ';'.join(courses) #output >History;Math;Physics;CompSci
print(new_courses)
split_courses = new_courses.split(sep=';')
print(split_courses) # --> returns the courses without the ; between them >['History', 'Math', 'Physics', 'CompSci'

#tuples 
# we cant modify tuples(imutable)
# Mutable
#list_1 = ['History', 'Math', 'Physics', 'CompSci']
#list_2 = list_1

#print(list_1)
#print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)
# ^the problem here is by changeing list1s first value we changed list twos as well

# tuple is like a list but wihth () insted of []
# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# returns a type error becuse tuples are immutable
# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets --> values that are unorderd and have no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)
# sets are used to remove duplicate values and check if someting is in the set
# sets are also used for a membership test ex: print('Math' in cs_course) > returns True
# can be used to chek the simalarity of the sets --> set.intesection(second_set) > returns common values
# set.diffrence(second_set) > returns diffrent values form the sets
# set.union(second_set) >like list.join but with sets


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict type
empty_set = set() # we need to use the set() to make an empty set

