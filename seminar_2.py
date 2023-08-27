import random, math
n = input("Number of coins ")
tails = n - random.randint(0,n)
heads = tails
print(min(heads,tails))


S = input("Sum of numbers x and y ")
P = input("Product of numbers x and y ")
x = (S + int(math.ceil(math.sqrt(S*S-4*P))))//2
y = S - x
print('x = ' + str(x) + ', y = ' + str(y))

N = input("Input integer N ")
r = 1
while (r < N):
    print(str(r))
    r *= 2