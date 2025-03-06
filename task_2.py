from re import findall

print('All the closing tags:')

closing_tags = set()
with open('task2.html', encoding='utf-8') as f:
    for row in f:
        matches = findall(r'</\w*>', row)
        closing_tags.update(matches)

print(*closing_tags, sep='\n')
            