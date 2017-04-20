# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases

def min_max_diff(list_of_numbers):
    the_max = list_of_numbers[0]
    for num in list_of_numbers:
        if the_max < num:
            the_max = num
    print(the_max)
    the_min = list_of_numbers[0]
    for num in list_of_numbers:
        if the_min > num:
            the_min = num
    print(the_min)


list_to_examine = [2, 3, 8]

print(min_max_diff(list_to_examine))

"""
max(list_of_numbers) = highest_value
min(list_of_numbers) = lowest_value
difference = highest_value - lowest_value
return difference"""
