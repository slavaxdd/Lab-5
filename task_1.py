from re import search

f = open('task1-en.txt', 'r')

# Все слова, начинающиеся с большой буквы; 
cap_let = []
# все слова, после которых стоит двоеточие.
colon = []

for row in f:
    match = search(r'\s[A-Z][a-z]+\s', row)
    if match:
        cap_let.append(match[0])
    match = search(r'\s[A-Z]?[a-z]+:\s', row)
    if match:
        colon.append(match[0])

print('All words starting with a capital letter:', *cap_let, sep='\n')
print()
print('All words ending with a colon:', *colon, sep='\n')