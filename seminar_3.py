k = 'notebook'

alphabet = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'):1,
            ('D', 'G'): 2,
            ('B', 'C', 'M', 'P'): 3,
            ('F', 'H', 'V', 'W', 'Y'): 4,
            'K': 5,
            ('J', 'X'): 8,
            ('Q', 'Z'): 10,
           }
k = k.upper()
sum = 0
print(alphabet.keys())
for c in k:
    for item in alphabet.keys():
        if c in item:
            sum += alphabet[item]
print(sum)
