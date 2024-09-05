my_set = {1, 2, 3}

print(my_set) # {1, 2, 3}
my_set.clear()
print(my_set) # {1, 2, 3}
my_set.add("A")
my_set.add("B")
print(my_set) # {1, 2, 3}
my_set.discard("c")

# Needed Output


# set()
# {"A", "B"}