import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
950-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

# Case ignoring
pattern_with_i = re.compile(r'start', re.I)
matches = pattern_with_i.search(sentence)
print(matches)

# Using anchor \b
pattern_with_anchor = re.compile(r'\bHa')
matches = pattern_with_anchor.finditer(text_to_search)
for match in matches:
    print(f"Found: {repr(match.group())} on {match.span()}")


# Phone number
pattern_phone = re.compile(r'[89]\d0[-.]\d\d\d[-.]\d\d\d\d')
with open ('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
matches = pattern_phone.finditer(contents)
for match in matches:
    print(f"Found: {repr(match.group())} on {match.span()}")


# Word with 3 symbols that finish on 'at' but not start with b
pattern = re.compile(r'[^b]at')


# Names
pattern_name = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z][a-z]*')
matches = pattern_name.finditer(text_to_search)
for match in matches:
    print(f"Found: {repr(match.group())} on {match.span()}")
