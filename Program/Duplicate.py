numbers = [2, 2, 3, 3, 4,2,3,4,4,2,5,6,7,7]

def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(get_unique_numbers(numbers))