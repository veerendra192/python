from random import *
ages = [randint(1,100) for i in range(1,100)]
print(ages)
children=[i for i in ages if i<13]
teen=[i for i in ages if i>13 and i<20]
adult=[i for i in ages if i>20 and i<50]
old=[i for i in ages if i<50]
print(children,"\n")
print(teen,"\n")
print(adult,"\n")
print(old,"\n")


