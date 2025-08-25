my_list = []
my_range = int(input("Enter range: "))
for i in range(my_range):
    num = int(input("Enter numbers: "))
    my_list.append(num)
add = 0
for i in my_list:
    add = add + i
print("the sum is",add)