import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# pattern = re.compile(r'Words you wanna find', re.I = (IGNORECASE)

# matches = pattern.search(Text name)

# 0 = whole groups / 1 = first group / 2 = second group / 3 = third group ...

# subbed_urls = pattern.sub(r'\2\3', urls)
#
# print(subbed_urls)

maches = pattern.finditer(urls)

for match in maches:
    print(match.group(0))
