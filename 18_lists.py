# list are order collection of item
marks = [3, 5, 6, "Om" , True,1,34,45,53,653,342,442]
print(marks)
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# if 5 in marks:
#     print("yes")
# else:
#     print("no")

# # for string
# if "m" in "om":
#     print("Yes")
# else:
#     print("no")

# print(marks[:])
# print(marks[2:4])
# print(marks[1:9:2])

# list comprehension 
# it is used for creating new lists from other iterables
lst = [i*i for i in range(6) if i%2==0]
print(lst)