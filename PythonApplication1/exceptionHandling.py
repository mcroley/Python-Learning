class exceptionHandling(object):
    """an example of handling exceptions"""

def exceptionThrownHere():
    """this function will always throw an assertion error """
    assert 1 == 7

try:
    exceptionThrownHere()
except AssertionError:
    print('Exception Handled right here')

class anotherClass():
    def tryAnotherFunc():
        total = 1 + 2
        return total
    print(tryAnotherFunc)
