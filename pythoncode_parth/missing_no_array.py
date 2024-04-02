def find_missing_number(arr):
    n = len(arr) + 1  # Including the missing number
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

array = [1, 2, 4, 6, 3, 7, 8]
missing_number = find_missing_number(array)
print("The missing number is:", missing_number)
