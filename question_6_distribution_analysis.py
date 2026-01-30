def percentage_less_or_equal(numbers):
    # Get the total number of elements in the list
    total_num_of_elements_in_list = len(numbers)

    # Dictionary to store the result:
    result = {}

    # Iterate through each unique number in sorted order
    for key in sorted(set(numbers)):
        # Count how many numbers in the list are less than or equal to the current key
        count = sum(1 for n in numbers if n <= key)
        # Calculate the percentage and store it in the result dictionary
        result[key] = (count / total_num_of_elements_in_list) * 100


    # Return the final dictionary
    return result


# Example list of numbers
numbers = [3,1,2,3,4,2]
# Print the percentage of values less than or equal to each unique number
print(percentage_less_or_equal(numbers))