
#Defines a function that receives a list of strings and returns a dictionary
def string_to_dictionary(list_of_strings):
    result = {}


#iterate over each string in list, compute string length, and save length and parity
    for string in list_of_strings:
        length_of_string = len(string)
        result[string] = {
            "length": length_of_string,
            "parity": "even" if length_of_string % 2 == 0 else "odd"
        }

    return result


#Testing the function and printing output
print(string_to_dictionary(["data","science"]))