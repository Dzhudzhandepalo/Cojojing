user = {
    "name": "John",
    "age": 23,
    "friends": [
        "Mike", "Bob", "Joe"
    ],
    "skills": ("HTML", "CSS", "JS"),
}

# 1) Find Mike into the user , than if u found Mike create a variable for him
# 2) Print Mike at the console
# 3) Get age of user , and guess when he was born
# 4) Skills must look as : Python , QA , Selenium
# 5) Sort john's friends
# 6) After sort find index position of "Bob"
# 7) Add new friends to friends : "Taras" , "Danya" , "Bidden"
# 8) Show how much skills user has

#1)***********************************************************
#Mike_solo = user["friends"][0] 

#2)***********************************************************
#print(Mike_solo)

#or u can do ----- print("Mike" in user)


#3)***********************************************************
# from datetime import datetime

# current_year = datetime.now().year

# Age_solo = user["age"]

# year_of_bearth = current_year - int(Age_solo)

# print(year_of_bearth)


#4)***********************************************************

# user["skills"] = ("Python" , "QA" , "Selenium")

# print(user["skills"])

#5)***********************************************************

# print(user["friends"])

# sorted_friends = sorted(user["friends"])

# print(sorted_friends)

# #6)*******

# Bob_index = user["friends"].index("Bob")

# print(Bob_index)


#7)***********************************************************
# print(user["friends"])

# # user["friends"].append("Taras")
# # user["friends"].append("Danya")
# # user["friends"].append("Bidden")

# or

# new_friends = ("Taras" , "Danya" , "Bidden")

# user["friends"].extend(new_friends)

# print(user["friends"])

#8)***********************************************************
# counted_skills = len(user["skills"])

# print(counted_skills)