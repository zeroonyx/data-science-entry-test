def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        raise TypeError("please input a string")
    #slice string with step -1 to reverse it.  
    #omit start and end to reverse the whole string.
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# demonstrations
print(string_reverse("Hello World"))
print(string_reverse("Python"))
