# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)
# my_list.extend(5)
# print(my_list)
my_list.append([9, 9, 9])
print(my_list)
# my_list.append(9, 9)
# insert
my_list = [1, 2, 3]
my_list.insert(1,5)
print(my_list)
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)
print(item2)
print(my_list)

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)

# count
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count)

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)
print(my_list.reverse())

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)