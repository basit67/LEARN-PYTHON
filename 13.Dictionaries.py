#Dictionaries - ket/value pair {}

drinks = {"white russain":7,"old fashion": 10, "lemon drop":8 } #drink is your key and price is your value
print(drinks)


employee = {"finace":["bob","shida","pina"], "IT": ["gene","grey"],"HR": ["jimmy","morty"]}
print(employee)
# this add to new key value pair
employee['legal'] = ['mr frond']
print(employee)
employee.update({"sales":["anny","olives"]})
print(employee)

#update key vale pair
drinks["white russain"] = 8
print(drinks)

#item out of the Dictionaries
print(drinks.get("white russain"))