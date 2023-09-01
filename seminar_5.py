
a = "a a a b c a a d c d d"
dict = {}
res = ""
for el in a.split():
    dict[el] = 0

for el in a.split():
    if dict[el] == 0:
        res = res + el + " "
    else:
        res += f"{el}_{dict[el]} "
    dict[el] = dict[el] + 1
print(res)

a = " She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
print(len(set(a.replace("."," ").lower().split())))