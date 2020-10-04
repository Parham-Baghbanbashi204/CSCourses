#fist class functions 
def squre(x):
    return x*x

#by not adding the parenthises we can set f to the acctual function
f = squre

# becuse f = function we can now call our function using f
f(5)

#higer order functions ex: pythons map function
# that function takes a function and an array
# essentaily higer order functions takes functions as arguments
"""
def html_tag(tag):
    # first class function that returns a function(tecnacly a closure)
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    # becuse there are no parentiseis the function is not run 
    # insted the function is set to the variable calling the html_tag function
    return wrap_text

#examples 
print_h1 = html_tag('h1')
# becuse this is now set to the wrap text function
# we can call the variable like its a function
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
"""

# python decorators tutorial
# we use first class functions for this tutorial

"""
A decorator is a first class fuction that executes a function by 
accepting a function as an argurment
all it does is takes a function and runs it with diffrent tasks
"""
