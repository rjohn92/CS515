# 
# ## CS 515
# ## Homework 3
# 

# ### 1. Conditionals
# 

# (1) Write a function that converts all units of time into seconds.
# The input is a list that indicates [days, hours, minutes, seconds]. 
# The list should at least includes the seconds element, other elements are optional.


def convert_time(alist):    
    """
        Functions to converts time into seconds.

        Examples:
            [5]:     5
            [1,5]:     65
            [1,2,3]:    3723

        Returns: converted seconds.
        
        Parameter: a list
        Precondition: a list has at least one element
    """
    return None


# ### 2. Testing
 
# Here is a function that is not working properly due to the special precondition. 
# Please use introcs.assert_equals() to test the result and indicate what is the problem of this function.
# Then, fix the function so it works correctly!!!
# Use introcs.assert_equals() again to make sure the input qualifies the precondition and test your result again. 
# (consider what n.find(' ') will return if the input is invalid)


def last_name_first(n):
    """
        A single, non-working function.

        The function in this module has a bug (in the sense that it does not satisfy its specification). This allows us to show off debugging.

        Returns: copy of n but in the form 'last-name, first-name'

        Parameter n: the person's name
        Precondition: n is in the form 'first-name last-name'
        with one or more blanks between the two names no spaces in <first-name> or <last-name>
    """

    end_first = n.find(' ')
    first = n[:end_first]
    last  = n[end_first+1:]
    
    return last+', '+first


# ### 3. Control Flow

# Function sortnum(). 
# This function takes three numbers as input and sorts the number from small to large (ascending order) 
# and returns the numbers. 
# Using only simple variables and if statements, you should be able to get this to work; 
# a loop is not needed (And SHOULD NOT BE USED!).



def sortnum(alist):
    """ 
        Returns: a list contains three numbers in ascending order. 
        Example: 
        >>>sortnum([2,1,3]) 
        >>>[1,2,3]

        Precondition: alist is a list that contains three numbers. 

    """
    return None

# ### 4. Challenge

# Write a function to anglicize the integers n where 0<n<1000, 
# for example, if the input is 5, the output should be 'five', if the input is 33, 
# the output should be 'thirty three'.



def anglicize(n):
    """
        Functions to anglicize integers in the range 1..999

        The primary function in this module is anglicize(). This is a
        great module to help you understand conditions.

        Examples:
            3:      "three"
            45:     "forty five"
            100:    "one hundred"
            127:    "one hunded twenty seven"
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 1..999
    """
    return None


def anglicize1to19(n):
    """
        Returns: English equivalent of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 1..19
    """
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    
    # n = 19
    return 'nineteen'


def anglicize20to99(n):
    """
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 20..99
    """

    #####Your code#####
    return None

def anglicize100to999(n):
    """
        Returns: English equiv of n.
        
        Parameter: the integer to anglicize
        Precondition: n in 100..999
    """
    # Anglicize the first three digits

    hundreds = n % 100
    suffix = ''
    
    #####Your code#####
    
    return anglicize1to19(n//100) + ' hundred' + suffix

def tens(n):
    """
        Returns: tens-word for n
        
        Parameter: the integer to anglicize
        Precondition: n in 2..9
    """
    #####Your code refer to anglicize1to19(n) #####
    return None

