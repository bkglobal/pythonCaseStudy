a = 1
x = 'One' if a==1 else 'Two'
print(x)

y = 'Even' if a%2 == 0 else 'Odd'
print(y)

def compareGreaterVsalue(num1, num2):
    return num1 if num1 > num2 else num2

print(compareGreaterVsalue(2,5))
