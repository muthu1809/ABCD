#str format
name = 'raja'
age = 22
print("1-> Hello {} Your age is {}".format(name,age))
print("2-> Hello {0} Your age is {1}".format(name,age))
print("3-> Hello {1} Your age is {0}".format(name,age))
print("4-> Hello %s Your age is %s".format(name,age))
print("5-> Hello {a}, Your age is{b}".format(a=name,b=age))
print("6-> Hello {a}, Your age is{b}".format(b=name,a=age))
#space holder