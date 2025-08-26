# my_list = []
# my_range = int(input("Enter range: "))
# for i in range(my_range):
#     num = int(input("Enter number: "))
#     my_list.append(num)
# my_list.reverse()
# print("Reversed list:", my_list)

#process 2
# my_list = []
# my_range = int(input("Enter range: "))
# for i in range(my_range):
#     num = int(input("Enter number: "))
#     my_list.append(num)
# reversed_list = my_list[::-1]
# print("Reversed list:", reversed_list)


#process 3
my_list = []
my_range = int(input("Enter range: "))
for i in range(my_range):
    num = int(input("Enter number: "))
    my_list.append(num)
rev_list = []
for i in range(len(my_list) -1, -1, -1):
    rev_list.append(my_list[i])
print(rev_list)


