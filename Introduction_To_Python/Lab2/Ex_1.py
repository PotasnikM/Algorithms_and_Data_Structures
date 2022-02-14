if __name__ == '__main__':
    # Creating list of values from <500,3000>
    list_of_values = [i for i in range(500, 3001)]
    string_of_values = ''
    for elem in list_of_values:
        # Checking if element in list fulfills the condition
        if elem % 7 == 0 and elem % 5 != 0:
            # Adding element into string
            string_of_values += str(elem)
    # Counting number of "21" in string
    number_of_encounters = string_of_values.count('21')
    # Replacing "21" with "XX"
    new_string = string_of_values.replace('21', 'XX')
