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

def testFun():
    print(2 + 3)
testFun()

#### Referencing another class' function - this references the function in Python2
s = 5
PythonApplication2.test(2)

#### Iterating over a List
numbers = [1, 2, 3,]
sum = 0
for x in numbers:
    sum += x
print(sum)

numbers.insert(1, 4)

if 3 in numbers: 
    print('true')
else:
    print("false")
# numbers.insert('Bob', 4) this won't work. Python knows the data type and will not allow a different data type in a List
print(numbers)

print(sorted(numbers))



dictz = {}
dictz['a'] = "test"
dictz['b'] = "right"

print(dictz['a'])
for a in dictz:
    print(a)


