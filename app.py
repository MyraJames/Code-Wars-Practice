# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    result = 0
    for  i in range(0, len(numbers)):
        result = result + numbers [i] ** 2
    print(result)
    return sum(x ** 2 for x in numbers)
    square_sum([1,2,2])
    

    # range() function returns a sequence of numbers, starting from 0 by default, 
    # and increments by 1 (by default), and stops before a specified number.
    
    # The len() function returns the number of items in an object. When the object is a string, 
    # the len() function returns the number of characters in the string.

    # When you use a range loop you are saying that you want to count one by one from one number until you hit another.
    # Typically it would look like this. for i in range(0, 5): 
    # This means I want to count from 0-4 and set i to the current loop I am currently on. 