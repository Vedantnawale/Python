name = "Vedant A Nawale"
print(len(name))
print(name[0:3]) # including 0 but not 4
print(name[1:3]) # including 1 but not 4
print(name[:3]) # it automatically count from 0
print(name[0:-3]) # it print(name[0:len(name)-3])
print(name[-1:-3]) # it print(name[len(name)-1:len(name)-3])
print(name[-3:-1]) # it print(name[len(name)-3:len(name)-1])