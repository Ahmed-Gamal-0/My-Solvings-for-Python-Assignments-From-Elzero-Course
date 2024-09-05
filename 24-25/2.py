friends = ("Osama", "Ahmed", "Sayed")

temp = list(friends)
temp[0] = "Elzero"
friends = tuple(temp)

print(friends) # ("Elzero", "Ahmed", "Sayed")
print((type(friends)))# <class 'tuple'>
print(len(friends)) # 3
