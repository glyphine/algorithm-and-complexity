def find_smallest_element(arr):
    n = len(arr)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        
        if arr[mid] < arr[mid - 1]:
            return arr[mid] 
        elif arr[mid] > arr[0]:
            left = mid + 1
        else:
            right = mid - 1

    return arr[left]

circular_array = [27, 29, 35, 42, 5, 15]
smallest_element = find_smallest_element(circular_array)
print("Smallest element in the circular array:", smallest_element)
