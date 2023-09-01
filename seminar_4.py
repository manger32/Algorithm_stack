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

# homework
#22
list_1 = []
list_2 = []
n = input("Input integer n ")
m = input("Input integer m ")
for i in range(0,n):
    x = input("input number from first set ")
    list_1.append(x)
for i in range(0,m):
    x = input("input number from second set ")
    list_2.append(x)
set_1 = set(list_1)
set_2 = set(list_2)
new_ordered_set = frozenset(sorted(set_1.union(set_2)))
print(new_ordered_set)

#24
N = input("Input integer N ")
a = []
for i in range(0,N):
    x = input("input number of berries on a bush ")
    a.append(x)
max_num = 0
for i in range(1,N-1):
    current = a[i-1] + a[i] + a[i+1]
    if max_num < current:
        max_num = current
current = a[0] + a[N-1] + a[N-2]
if max_num < current:
        max_num = current
current = a[0] + a[1] + a[N-1]
if max_num < current:
        max_num = current
print(max_num)