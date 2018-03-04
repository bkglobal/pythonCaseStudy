from re import *
regex = "\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+"
pattern = compile(regex)
address = input ('input the email address: ')
is_valid = pattern.match(address)
if is_valid:
    print('Valid Email Address ',is_valid.group(),is_valid.start(), is_valid.end())
else:
    print('InValid Email Address')