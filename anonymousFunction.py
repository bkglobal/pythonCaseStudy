square = lambda x : x**2
square_queue= [lambda x : x**0, lambda x : x**1, lambda x: x**2, lambda x : x**3, lambda x : x**4]

print(square(4))
print(square_queue[4](2))
