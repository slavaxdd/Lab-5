from re import findall
import csv

DATA = []

ID = []
surname = []
email = []
reg_date = []
site = []


with open('task3.txt', 'r') as f:
    file_content = f.read()
    matches1 = findall(r'(?<![\w-])[0-9]+(?![\w-])', file_content)
    ID.extend(matches1)
    matches2 = findall(r'[A-Z][a-z]*', file_content)
    surname.extend(matches2)
    matches3 = findall(r'[0-9a-zA-Z_-]+@[0-9a-zA-Z_-]+\.[a-z]+', file_content)
    email.extend(matches3)
    matches4 = findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', file_content)
    reg_date.extend(matches4)
    matches5 = findall(r'https?://[0-9a-zA-Z_-]+\.?[0-9a-zA-Z_-]+\.[a-z]+/', file_content)
    site.extend(matches5)



for i in range(len(ID)):
    DATA.append([ID[i], surname[i], email[i], reg_date[i], site[i]])

#print(*DATA, sep='\n')


with open('task_3_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(DATA)