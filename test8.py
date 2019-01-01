import csv

html_output = ''
names = []

with open('파일명', 'r, a, w') as alias:
    csv_data = csv.DictReader(alias)

    next(csv_data)
    # Skip the first element in Iterable data

    for line in csv_data:
        if line['Key name'] == 'useless info':
            break
        names.append(line['Key name '] + line['Key name'])

html_output += '\n<ul>'

for name in names:
    html_output += f'<li>{name}</li>\n'

html_output += '\n</ul>'

print(html_output)
