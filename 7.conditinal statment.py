import re


def drink(money):
    if money >= 2:
        return "you got drink"
    else:
        return "no drink for you"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >=5):
     return "here your drink"
    elif  (age >= 21) and (money <=5):
     return "come back with money"
    elif (age < 21) and (money >= 5):
     return "nice try, kid!"
    else:
     return "you are too poor and too young"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
print(alcohol(19,100))