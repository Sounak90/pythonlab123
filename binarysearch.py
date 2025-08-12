# def binary_search(my_array,element):
#     left = 0
#     right = len(my_array) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if my_array[mid] == element:
#             return mid
#         elif my_array[mid] < element:
#             left = left + 1
#         else:
#             right = right - 1
#     return -1
#
#
# arr = [1,2,3,4,5,6,7.8]
# target = int(input("Enter a Number: "))
# binary_search(arr,target)

def binary_search(my_array, element):
    left = 0
    right = len(my_array) - 1

    while left <= right:
        mid = (left + right) // 2
        if my_array[mid] == element:
            return mid
        elif my_array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
try:
    target = int(input("Enter a Number: "))
    index = binary_search(arr, target)
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found.")
except ValueError:
    print("Please enter a valid number.")
