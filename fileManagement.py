poem = 'never saw a man who looking\n'
poem += 'with such  wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

file = open('poem.txt','w')
file.write(poem)
file.close()

file = open('poem.txt','r')
for line in file:
    print(line, end="")
file.close()

with open('poem.txt','r+') as f:
    text = f.read()
    print(text)
print(f.closed)