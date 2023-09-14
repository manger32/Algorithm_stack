#! /usr/bin/env python
# -*- coding: utf-8 -*-

#34
def ParamParam(cnt, str):
    vowels = []
    for word in str.split(" "):
        vowels.append(cnt(word))
    return all(i == vowels[0] for i in vowels)

def countVowels(str):
    char = [*str]
    print(char)
    set_vowels = set(("а","о","е","ё","и","я","у","о","ы","э","ю"))
    count = 0
    for i in char:
        if i in set_vowels:
            count += 1
    return count

str_p = input("Введите речь Винни-Пуха ")
if ParamParam(countVowels, str_p):
    print("Парам пам-пам")
else:
    print("Пам парам")
# пара-ра-рам рам-пам-папам па-ра-па-да

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1,num_rows + 1):
        for j in range(1,num_columns + 1):
            print(str(operation(i,j)) + " ", end="")
        print("\n", end="")

print_operation_table(lambda x, y: x*y)
