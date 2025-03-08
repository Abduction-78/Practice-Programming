def count_valid_numbers():
    valid_numbers = set()
    
    for digit1 in range(1, 10):
        for digit2 in range(digit1 + 1, 10):
            for d1 in [digit1, digit2]:
                for d2 in [digit1, digit2]:
                    for d3 in [digit1, digit2]:
                        number = str(d1) + str(d2) + str(d3)
                        if number[0] != number[1] or number[1] != number[2]:
                            valid_numbers.add(number)
    
    return len(valid_numbers)


result = count_valid_numbers()
print(result)
