friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

#Needed Output => "Ahmed", "Sayed", "Ali",
#order in list =>    2        3       4
#indexes       =>    1        2       3
print(friends[1:4])



#Needed Output => "Ali", "Mahmoud"
#Needed Output => "Ali",            |  "Mahmoud"
#order in list =>   4               |     5
#indexes       =>  before last name |   last name
print(friends[len(friends) - 2 : ])

