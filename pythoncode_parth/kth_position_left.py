def rotate_array_left_by_k(arr, k):
    n = len(arr)
    k = k % n

    if k == 0 or n <= 1:
        return arr

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


array = [1, 2, 3, 4, 5]
k = 2
print("Original array:", array)
rotate_array_left_by_k(array, k)
print("Array after rotating left by", k, "positions:", array)
