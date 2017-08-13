import sys
import PythonApplication2
#### String example
b = 'hello world '
z = 1
#### concating a string with an int using Python's str function:
print(b + str(z))
#### Python length function:
print(len(b))
print(b[1])

#### Function example
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
fib(1000)
s = 5
#### Referencing another class' function
PythonApplication2.test(2)

#### Iterating over an array
numbers = [1, 2, 3]
sum = 0
for num in numbers:
 sum += num
print(sum)

#### updating the 

#list = ['larry', 'curly', 'moe']
#if 'curly' in list:
# print('yay')


