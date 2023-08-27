#1
import random, math
n = input("Number of coins ")
tails = n - random.randint(0,n)
heads = tails
print(min(heads,tails))

#2
S = input("Sum of numbers x and y ")
P = input("Product of numbers x and y ")
x = (S + int(math.ceil(math.sqrt(S*S-4*P))))//2
y = S - x
print('x = ' + str(x) + ', y = ' + str(y))

#3
N = input("Input integer N ")
r = 1
while (r < N):
    print(str(r))
    r *= 2

#4
Inumber = input()
NumberOfDigits = 0
while (Inumber % 1 != 0):
    Inumber = Inumber * 10
Inumber = int(Inumber)
print(Inumber)
while Inumber != 0:
    Inumber = Inumber / 10
    NumberOfDigits += 1
print(NumberOfDigits)
#5
nums = []
for i in range(1,20):
    nums.append(random.randint(-10,10))
print(nums)
resulting_sequence = []
temporary_sequence = []
for i in range(1,19):
    if nums[i-1] < nums[i]:
        temporary_sequence.append(nums[i-1])
    else:
        temporary_sequence.append(nums[i-1])
        if (len(temporary_sequence) > len(resulting_sequence)):
            resulting_sequence = temporary_sequence
        temporary_sequence = []
print(resulting_sequence)