list1 = [2, 3, 4, 5]
list2 = [3, 4, 6, 7]
intersec = []
for element in list1:
    if element in list2 and element not in intersec:
        intersec.append(element)
print(intersec)