import sys
import PythonApplication2
#### String example
b = 'hello world '
z = 1
#### concating a string with an int using Python's str function:
print('concating' + b + str(z))

#### Python length function:
print(len(b))
print(b[1])

#### Function example
def fibanaci(n):
     a, b = 0, 1
     while a < n:  # indents show what should be included with a loop
         print(a, end=' ')
         a, b = b, a+b
     print()
fibanaci(1000)

#### Referencing another class' function - this references the function in Python2
s = 5
PythonApplication2.test(2)

#### Iterating over an array
numbers = [1, 2, 3]
sum = 0
for num in numbers:
 sum += num
print(sum)


#list = ['larry', 'curly', 'moe']
#if 'curly' in list:
# print('yay')


