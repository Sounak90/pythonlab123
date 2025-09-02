arr = []
for i in range(6):
    num = int(input("Enter the number: "))
    arr.append(num)
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)