# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
     return "".join(x.split()) 
    
x = ' 8 j 8   mBliB8g  imjB8B8  jl  B '
print(no_space(x))

# First we use split() function to return a list of the words in the string,
# using sep as the delimiter string. Then, we use join() to concatenate the iterable.

# The sep parameter is primarily used to format the strings that need to be printed on the
# console and add a separator between strings to be printed. 
# This feature was newly introduced in Python 3. x version

# Python: Split a string with multiple delimiters
# Note : A delimiter is a sequence of one or more 
# characters used to specify the boundary between separate, independent
# regions in plain text or other data streams

# The join() method takes all items in an iterable and joins them into one string.

# concatenate means link (things) together in a chain or series

# iterable (plural iterables) (programming) An object that can be iterated over.
# make repeated use of a mathematical or computational procedure, applying it each time to
#  the result of the previous application; perform iteration.


