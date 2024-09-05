# Create Dictionary Here
mySkills = {
    "skill 1"  : {
        "language" : "HTML",
        "Progress" : "90%"
        },
    
    "skill 2" : {
        "language" : "CSS",
        "Progress" : "80%"
        },
    
    "skill 3" : {
        "language" : "Python",
        "Progress" : "30%"
        },
    
    "skill 4" : {
        "language" : "AI",
        "Progress" : "20%"
        }   
}

#first way
mySkills.update({"skill 5": {"language" : "C++", "Progress" : "40%"}})

print(mySkills["skill 1"])
print(mySkills["skill 2"])
print(mySkills["skill 3"])
print(mySkills["skill 4"])
print(mySkills["skill 5"])




# second way
new_skill = {
    "language" : "C++",
    "Progress" : "40%"
    }

mySkills["skill 5"] = new_skill
print(mySkills["skill 1"])
print(mySkills["skill 2"])
print(mySkills["skill 3"])
print(mySkills["skill 4"])
print(mySkills["skill 5"])





