import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern_url = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern_url.sub(r'\2\3', urls)
print(subbed_urls)

matches = pattern_url.finditer(urls)

for match in matches:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
