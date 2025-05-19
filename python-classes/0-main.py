#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))           # <class '0-square.Square'>
print(my_square.__dict__)        # {'_Square__size': 3}

try:
    print(my_square.size)        # AttributeError: 'Square' object has no attribute 'size'
except Exception as e:
    print(e)

try:
    print(my_square.__size)      # AttributeError: 'Square' object has no attribute '__size'
except Exception as e:
    print(e)
