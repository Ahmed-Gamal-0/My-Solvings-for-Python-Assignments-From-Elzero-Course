nums = {1, 2, 3}
letters = {"A", "B", "C"}

#first way
print(nums.union(letters))

#second way
print(nums | letters)

#third way
nums.update(letters)
print(nums)
