import re
text ='''
abccdefghijklmnopqrstuvqxyz
ABCCDEFGHIJKLMNOPQRSTUVQXYZ
123567890

Ha HaHA

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
800.555.1234
900.555.1234

Mr. Shafer
Mr Smitch
Ms Davis
Mrs Robinson
Mr. T
 
CoreyMShafer@gmail.com
corey.shafer@university.edu
corey-321-shafer@my-work.net
'''
pattern=''
######       TELEPHONE NUMBERS
#pattern=re.compile(r'((?:\d{3}-){2}\d{4})|((?:\d{3}\.){2}\d{4})')
#pattern=re.compile(r'(?:\d{3}\W){2}\d{4}')
#pattern=re.compile(r'(?:\d{3}[-\.]+){2}\d{4}')
#pattern=re.compile(r'(?:(?:[89]00|\d{3})[-\.]){2}\d{4}')
######       NAMES
#pattern=re.compile(r'M(?:[rs]|(?:rs))\.?\s [a-zA-Z]+')
#pattern=re.compile(r'((?:Mrs|Mr|Ms)\.?\s[a-zA-Z]+)')
######       EMAILS
#pattern=re.compile(r'([a-zA-Z-\.0-9]+@[a-zA-Z-]+.(?:com|edu|net))')
matches = pattern.finditer(text)
for match in matches:
    print(match.groups())
