# my_list = []
# my_range = int(input("Enter range: "))
# for i in range(my_range):
#     num = int(input("Enter number: "))
#     my_list.append(num)
# if my_list:
#     highest = max(my_list)
#     lowest = min(my_list)
#     print("Maximum number is:", highest)
#     print("Minimum number is:", lowest)
# else:
#     print("The list is empty.")


#process 2
my_list = []
my_range = int(input("Enter range: "))
for i in range(my_range):
    num = int(input("Enter number: "))
    my_list.append(num)
maximum = my_list[0]
for j in my_list:
    if j > maximum:
        maximum = j
print(maximum)
minimum = my_list[0]
for j in my_list:
    if j < minimum:
        minimum = j
print(minimum)
