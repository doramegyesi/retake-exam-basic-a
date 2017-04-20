# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases

def min_max_diff(list_of_numbers):
    try:
        the_max = list_of_numbers[0]
        for num in list_of_numbers:
            if the_max < num:
                the_max = num
        the_min = list_of_numbers[0]
        for num in list_of_numbers:
            if the_min > num:
                the_min = num
        difference = the_max - the_min
        return difference
    except IndexError:
        print(None)    

list_to_examine = [2, 3, 8]
another_list = [5, 21, 68, 71, 105, 33]

print(min_max_diff(list_to_examine))
print(min_max_diff(another_list))
