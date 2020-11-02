""" Regular Expressions is a python module that allows us to look
    for particular strings of characters within text documents. 
    This is a short lesson on how to use the re or Regular Expressions
    module in python 3.8
"""

import re
from sre_constants import SRE_FLAG_IGNORECASE

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):

. ^ $ * + ? { } [ ] \ | ( )

tuckerc.com

323-452-6987
123.555.1234
542*547*4578
800-578-6987
900-987-8741

Mr. Celestine
Mr Smith
Ms Danish
Mrs. Robinson
Mr. T

cat
mat
pat
bat


'''

emails = '''
JoshuaTCelestine@gmail.com
joshua.celestine@university.edu
joshua-321-celestine@my-work.net

'''
urls ='''
https://www.google.com
http://tuckeryms.com
https://youtube.com
https://www.nasa.gov

'''
# raw strings are prefixed with an r like f strings. The tell python not to handle
# backslashes see tab example below
# print('\tTAB')
# print(r'\tTAB')

sentence = 'Start a sentence and then bring it to an end'

# How to search search a string of variables for patterns using re.
# First pattern string by passing the string as a raw string 
# to re.compile(). A backslash allows you to escape a character, remember . examples
# Also, see metacharacters_snippets.txt for a legend of arguments operations.
# pattern = re.compile(r'\.')
# pattern = re.compile(r'.')

# Matching the digits above to get both strings of numbers with - and dot
# use . wild card operator with \d (digits).
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# Matching using more complex arguments [-.] specifies either the - or . as
# the seperator for the numbers in the above list
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# Matching ranges [1-5] matches for numbers in the range of 1 to 5.
# The range queries can be compounded if typed back to back. Example
# [a-zA-Z]
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-zA-Z]')

# If you want to negate a character in the query for example if we wanted
# to return the words that end in at from the string above, cat, pat, mat and not bat
# we need to negate the b using the ^ inside of a [] brackets. This tells re that
# we do not want strings that match b....

# pattern = re.compile(r'[^b]at')


# Learning Quantifiers: Matching Mr from the above string. Using \. makes
# it so we aren't passing . as a wildcard.So, re.compile(r'Mr\.') takes the
# decimal to be literal and not a wildcard.If you want to see both the Mr & Mr.
# matches then we need to use the ? which denotes 0 or more so with a decimal
# or without one.
# pattern = re.compile(r'Mr.')
# pattern = re.compile(r'Mr\.')
# pattern = re.compile(r'Mr\.?')

# The below match string reads Mr where . isnt wild, with a decimal or not, whitespace,
# capitals between A-Z, any lowercase letter, where there are 1 or more lowercase letters.
# The asterix is a better quantifier as it specfies 0 or more lowercase letters so
# we are able to read Mr. T as well
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# Using groups to match Mr, Ms, Mrs. Use the parenthesis to specify
# characters to match, the | denotes either/or . 
# pattern = re.compile (r'M(r|s|rs)\.?\s[A-Z]\w*')

# Initiate the pattern variable for matches and use the object to iterate
# through as the argument for finditer()
# matches = pattern.finditer(text_to_search)
#  
# for match in matches:
#     print(match)

# with open ('re_data.txt', 'r', encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

    
# check abc search for indexes [1:4]    
# print(text_to_search[1:4])

#######################################################################
#######################################################################
#######################################################################

# Regular expression for matching emails generic string of args. 
# Understand this!
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#  
# matches = pattern.finditer(emails)
#  
# for match in matches:
#     print(match)



# Search through and match the url strings with re.compile() for the 
# specific urls in the object above. Learn groups and how to sub group data
# for instances. 
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# 
# subbed_urls = pattern.sub(r'\2\3', urls)
# 
# print(subbed_urls)
# matches = pattern.finditer(urls)
# 
# for match in matches:
#     print(match.group(2))  
    
pattern = re.compile(r'Start')

# using match only returns the first match
# matches = pattern.match(sentence)
# print(matches)

# using findall returns all matches using a for loop to iterate
# matches = pattern.findall(sentence)

# Finds mathches throughout the entire string and 
# returns them without a loop
# matches = pattern.search(sentence)
# print(matches)

# for match in matches:
#     print(match)

# pattern = re.compile(r'start', SRE_FLAG_IGNORECASE)
# 
# matches = pattern.search(sentence)
# 
# print(matches)    