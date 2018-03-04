import sys, keyword
print(keyword.iskeyword('pass'))
print(sys.version)
print('System Path directories are:')
for dir in sys.path:
    print(dir)

print('Keywords are: ')
for word in keyword.kwlist:
    print(word)

