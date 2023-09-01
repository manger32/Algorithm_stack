string = "a a a b c a a d c d d"
dict = {}
for i in string.split(" "):
    dict[i] = 0
for i in string.split(" "):
    dict[i] += 1
res = ""
string = string[::-1]
for i in string.split(" "):
    if (dict[i] == 0):
        res += i + " "
    res += i + "_"+str(dict[i]-1) + " "
    dict[i] -= 1
res = " ".join(res.split(" ")[::-1])
res = res.replace("_0","")
print(res)

