def reverse_number(number):
    reversed_number = 0
    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number // 10
    return reversed_number

number = 12345
reversed_num = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_num)
