def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)

    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

    return sum_of_powers == num


number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
