tup = (1,6,42,5)
print(type(tup),tup)
if 42 in tup:
    print('Yes this number is present in tupple')
else:
    print("No")
tup1 = tup
print(tup1)
print(tup[2:4])
print(tup[1:4:2])