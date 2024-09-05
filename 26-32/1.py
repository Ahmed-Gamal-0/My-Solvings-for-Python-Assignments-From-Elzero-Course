my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = set(my_list)
unique_list = list(unique_list)

print(unique_list) # 1, 2, 3, 4, 5
print(type(unique_list))# <class 'list'>
unique_list.pop(-1)
print(unique_list) # 1, 2, 3, 4 





