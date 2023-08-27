countries = ("india","USA","russia","china","UK")
temp = list(countries)
temp.append("Nepal") # add item
print(temp)
temp.pop(2)  # remove item
temp[3]="Finland" # change item
print(temp)
print(type(temp))
countries = tuple(temp)
print(countries)
print(type(countries))