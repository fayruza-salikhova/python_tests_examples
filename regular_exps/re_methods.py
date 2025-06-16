import re

# re.match(pattern, string)
# Match from the beginning of the string. Returns a match object or None.
re.match(r'\d+', '123abc')  # matches '123'
re.match(r'\d+', 'abc123')  # returns None

# re.search(pattern, string)
# Search anywhere in the string. Returns the first match.
re.search(r'\d+', 'abc123def')  # matches '123'

# re.findall(pattern, string)
# Return all non-overlapping matches in the string as a list of strings.
re.findall(r'\d+', 'abc123def456')  # ['123', '456']

# re.finditer(pattern, string)
# Return an iterator yielding match objects over all matches.
for match in re.finditer(r'\d+', 'abc123def456'):
    print(match.group())  # '123', then '456'
    print(match.start(), match.end())  # position info

# re.sub(pattern, repl, string)
# Replace all occurrences of the pattern with the replacement string.
text = "My number is 123-456-7890"
re.sub(r'\d', 'X', text)  # 'My number is XXX-XXX-XXXX'

# re.split(pattern, string)
# Split the string by the occurrences of the pattern.
text = "apple,banana;orange|grape"
re.split(r'[;,|]', text)  # ['apple', 'banana', 'orange', 'grape']

# re.compile(pattern)
# Compile a pattern into a regex object for repeated use (better performance).
pattern = re.compile(r'\d+')
pattern.findall('a1b22c333')  # ['1', '22', '333']

# Match object methods (used with re.match/search/finditer)
m = re.search(r'\d+', 'abc123xyz')
if m:
    m.group()   # the full matched text, e.g., '123'
    m.start()   # start index of the match
    m.end()     # end index (exclusive)
    m.span()    # tuple of (start, end)
