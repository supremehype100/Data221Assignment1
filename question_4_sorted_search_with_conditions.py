from random import random


#Making a list of 20 random values then sorting it
values = [random() for i in range(20)]
x = random()

values.sort()

#Tracking indicies than adding value to last index if value>=x
indices = []

for index,value in enumerate(values):
    if value>=x:
        indices.append(index)


#Printing output and error handling
print("Sorted list:", values)
print("x:", x)

if indices:
    print("First index where value >= x:", indices[0])
else:
    print("No value in the list is greater than or equal to x.")
