# working with textual data

# text data is called a string
message = 'Hello World'

# we can quote quotes by using an escape charactor
mesagge_single_quote = 'bobby\'s world'

message_double_quotes = "bobby's world"

# depending on the type of string we can use "" or '' if a quote is already inside

multi_line_sting = """Bobby's world was a 
good carton in the 90s"""

# we can think of our string as a string with multiple charachtors
print(len(message))

# accsesing specific charactors using thier index
print(message[0]) # H
print(message[10]) # d

#from start to 4th index not includes fith index 
print(message[0:5]) #Hello

# prints form sixth index to the end
print(message[6:])

print(message)

greeting = 'hello'
name = 'Michel'

# string concatnation
new_message = greeting,name # --> adds space between greating and name using the comma

# formated string
new_message_format = '{}, {}. Wellcome'.format(greeting, name)

# f strings --> you can run code within the placeholder
new_message_f_strings = f"{greeting.upper()}, {name}. Welcome!."

# we can use dir to print methods/attributes
print(dir(name))

# we can find information for methods and classes using help(class.method)
print(help(str))

"""
string methods 
.lower() --> sets all charachtors to lowercase
.upper() --> sets all charachtors to upercase
.count('l') --> looks for ever instance of l and counts the amount of times it is refrances
.find('l') --> checks if l is present
.replace('Part to replace', 'replacement string') --> replaces part to replace with replacement string
"""