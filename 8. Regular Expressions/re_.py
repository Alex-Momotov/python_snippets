import re

#   Some sample text to work with
text = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

cat
mat
pat
bat
abc

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.12345
123*555*1234
800--555-4321
900-555-4321

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

#%% Raw strings
#   When working with regular expressions we will be using raw strings a lot.
#   Raw strings are strings denoted with 'r' in front of the string, e.g. r'someString'
#   Raw strings tell Python to treat them literally and avoid treating slashes or escape characters differently.
print('\tTab')
print(r'\tTab')

#%% re.compile(r'regex')
#   Allows to save a regular expression as a regular expression variable
#   Don't forget to specify the regular expression as a raw string
pattern = re.compile(r'abc')
print(type(pattern))

#%% re.compile(r'regex', flags)
#   flags is the optional parameter which configures our expression to do different things.
#   re.IGNORECASE       ignores letter case
#   re.ASCII            Make \w, \W, \b, \B, \d, \D, \s and \S perform ASCII-only matching instead of full Unicode matching. In other words, disables non ASCII matching.
#   re.MULTILINE        When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line and the pattern character '$' matches at the end of the string and at the end of each line
sentence = 'StArT a sentence and then bring it to an end'
pattern = re.compile(r'start', re.IGNORECASE)
match = pattern.search(sentence)
print(match)

#%% pattern.finditer(text)
#   Returns an iterator yielding match objects using the provided pattern.
#   We can then iterate through it to see all matches.
#   span=(start, finish) Tells us indexes of the string where the match was found.
pattern = re.compile(r'\d{3}.+\d{3}.+\d{4}')
matches = pattern.finditer(text)
for match in matches:
    print(match[0])
    print(match)

#%% pattern.findall(text)
#   If pattern doesn't contain strings, returns a list of all matched strings.
#   If pattern contains groups, returns a list of groups (tuple of groups if more than one group)
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.findall(text)
print(matches)

#%% pattern.sub(repl, text)
#   Returns original string text, but the matched substrings found with the pattern are replaced with repl string.
#   Within the repl string we can reference groups of matched pattern by using backslash+gr_num e.g. r'\2\3'
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_text = pattern.sub(r'This is a replacement \2\3', text)
print(subbed_text)

#%% pattern.match(text)
#   Searches only the beginning of the string and returns a match object. None if not found.
pattern = re.compile(r'\n.*bc')
matches = pattern.match(text)
repr(matches.group(0))

#%% pattern.search(text)
#   Searches the entire string and returns the first string that matched the pattern as a match object.
#   Returns None if the pattern was not found.
pattern = re.compile(r'[^b]adt')
matches = pattern.search(text)
if matches:
    print(matches[0])

#%% match.span()
#   Every match returned from the iterator function is an object and it has a span() function.
#   It returns a tuple of indices where the match was found. Those exact indices can be used to slice the original string.
print(match.span())
start, finish = match.span()
print(text[start:finish])

#%% match.group(0)
#   Returns just the matched string itself, because it is the group zero.
print(match.group(0))

#%%
pattern = re.compile(r'\S')
matches = pattern.finditer(text)
for match in matches: print(match.group(0))


























