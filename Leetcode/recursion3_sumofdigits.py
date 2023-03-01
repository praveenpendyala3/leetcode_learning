# Find sum of digits of a number with recursion


def sum_of_digits(num):
    if num//10 == 0:
        return num

    return num%10 + sum_of_digits(num//10)

print(sum_of_digits(1))


