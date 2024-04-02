def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_even_odd(array)
print("Number of even integers:", even_count)
print("Number of odd integers:", odd_count)
