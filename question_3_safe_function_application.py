
#Function that computes x^y given a list of pairs x, and y.
def compute_power(x,y):
    return x**y


#Given list of powers
pairs = [[5,2],[3,-1],[4,3],[2,0]]

#Computing powers from given list
list_of_computed_powers = []
for x,y in pairs:
    if y<0:
        continue
    list_of_computed_powers.append(compute_power(x,y))


#Printing list of computed powers
print(list_of_computed_powers)