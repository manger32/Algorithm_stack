import random
def arithmetic_sequence(a1, d, n):
    arithm = []
    for i in range(1,n+1):
        arithm.append(a1+(i-1)*d)
    return arithm

a1 = input("First arithmetic sequence element ")
d = input("Step of arithmetic sequence ")
n = input("Number of elements in sequence ")

print(arithmetic_sequence(a1,d,n))

def is_in_range(list_l, lower, upper):
    indices_list = []
    for i in range(0, len(list_l)):
        if list_l[i] > lower and list_l[i] < upper:
            indices_list.append(i)
    return indices_list

inp_n = input("Number of elements in list ")
list_l = []
for i in range(0,inp_n):
    list_l.append(random.randint(0,100))
print(list_l)
lower_bound = input("Lower ")
upper_bound = input("Upper ")
print(is_in_range(list_l,lower_bound,upper_bound))