def find_max():

    input_number = input("Enter the numbers: ")
    numbers = list(input_number)
    max_number = numbers[0]
    for item in numbers:
        if item > max_number:
            max_number = item

    return max_number