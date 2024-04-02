def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1

    while start_index < end_index:
        # Swap elements at start_index and end_index
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        # Move towards the center of the array
        start_index += 1
        end_index -= 1


original_array = [1, 2, 3, 4, 5]
print("Original array:", original_array)
reverse_array(original_array)
print("Reversed array:", original_array)
