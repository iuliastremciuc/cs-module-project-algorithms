def divides_self(num):
    """ Takes in a positive integer and determines if the number "devides itself"
    input: integer
    output: Boolean

    >>> divides_self(128)
    True
    >>> divides_self(12)
    True
    >>> divides_self(120)
    False
    """
    # Plan 
    # What happen if num equals 0
    # if num less or  equals 0
        #return False
    # if num is less than 10
        # return True

    # split into individual digits and 
    # loop through each digit in num 
       # if digit doesn't  evenly divide into num
            # return False

    # if we get through all of the digits 
        # return True   


    # Going to need modulo (even devision)
    # May need split
    # Need method for isolating each digit in the num

    pass

# Reverse the list first and then iterate until empty string
def tallest_building(lst):
    # Plan
    # Iterate through lst and remove empty strings
    lst = [x for x in lst if not x.isspace()]
    # lst = [x for x in lst if x.strip()]

    # return length of new lst multiplied by 20 and format with 'm'
    return str(len(lst) * 20) + 'm'
    # Need to distinguish between empty and non-empty (open sky) strings

"""
When coloring a striped pattern, you may start by coloring each square sequentially, 
meaning you spend time needing to switch coloring pencils.

Create a function where given a list of colors cols, 
return how long it takes to color the whole pattern. Note the following times:

It takes 1 second to switch between pencils.
It takes 2 seconds to color a square.

color_pattern_times(['Red', 'Blue', 'Red', 'Blue', 'Red']) # --> 14  
"""    

def color_pattern_times(cols):
    # TODO: inefficient, improve on second-pass
    # Plan 
    cols_len = len(cols)
    # if len(cols) is <= 1
    if cols_len <= 1:
        return cols_len * 2
        # return len * 2
    # len(col) * 2 is time spent coloring
    coloring_time = cols_len * 2
    # need to compute time spent switching
    switch_count = 0
    # iteration through cols starting at second item
    for i in range(1, cols_len):
        if cols[i] != cols[i-1]:
            switch_count += 1
        # if current col is different than prev col (this is a switch)
            # increment witch_count
    # return time spet coloring + switch_count
    return coloring_time + switch_count


"""
Create a function that takes two numbers as arguments (num, length) 
and returns a list of multiples of num up to length.

Ex:
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]

"""

def lis_of_multe(num, length):
    
    # Plan
    # initialize empty list
    lst = []
    # for i in range (1, length + 1)
    # length is the last in a range
    # creating an array of multiples up to length

    for l in range(1, length + 1):
        lst.append(l * num )
    return lst
print(lis_of_multe(4, 7))

