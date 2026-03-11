def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    #while loop to iterate through the list
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]  # Return the first negative number
        i += 1
    return "No negatives"  # Output if no negative number is found



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
#test cases
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Output: -1
print(find_first_negative([2, 10, 7, 0]))          # Output: "No negatives"
