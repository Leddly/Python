import json
from urllib.request import urlopen

people_string = '''
{
    "people": [
        {
        "name": "John Smith",
        "phone": "615-555-7164",
        "email": ["Johnsmith@gmail.com", "Johnsmith@naver.com"],
        "license": false
        },
        {
        "name": "Sara Corner",
        "phone": "614-451-8562",
        "email": ["Saraco@gmail", "Sacor@naver.com"],
        "license": true
        }
    ]
}
'''

# data = json.loads(people_string)
#
# print(data)
#
# for person in data['people']:
#     print(person)
#     del person['phone']
#
# new_data = json.dumps(data, indent=2, sort_keys=True)
# print(new_data)
#
# with open('파일명', 'r') as f:
#     data = json.loads(f)
#
# for Key_name in data['Key_name']:
#     print(Key_name['Key_name'])

with urlopen("https://github.com/druid-io/pydruid/issues/123") as url:
    source = url.read()

data = json.loads(source)

print(json.dumps(data, indent=2))
