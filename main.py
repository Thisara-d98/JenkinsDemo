import pytest
def AddNumbers(n1,n2):
    return n1+n2
def SubtractNumbers(n1,n2):
    return n1-n2
if __name__ == '__main__':
    number1=23
    number2 =45
    res=AddNumbers(number1,number2)
    res2=SubtractNumbers(number2,number1)
    print(res)
    print(res2)
