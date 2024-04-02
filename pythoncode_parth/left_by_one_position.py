def rotate_array_left(arr):
    if len(arr) <= 1:
        return arr

    first_element = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[-1] = first_element

array = [1, 2, 3, 4, 5]
print("Original array:", array)
rotate_array_left(array)
print("Array after rotating left by 1 position:", array)
