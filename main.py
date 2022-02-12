import re

EVEN_PREFIX = 'Even'
ODD_PREFIX = 'Odd'

def a(number):
    snumber = str(number)
    result = ''
    for i in snumber:
        if int(i) % 2 == 0:
            result += EVEN_PREFIX + i
        else:
            result += ODD_PREFIX + i

    return result


def b(my_input):
    result = ''
    stack = []
    for i in str(my_input):
        if i.isdigit():
            for j in stack[:]:
                result += stack.pop()
            result += i
        else:
            stack.append(i.upper())

    return result


def c(my_input):
    result = ''
    for i in my_input:
        if i.isdigit():
            result += str(i)
            continue
        result += str(ord(i))

    return result


def d(my_input):
    result = ''
    index = 0
    while True:
        if index > len(my_input)-1:
            break
        if my_input[index] == '6':
            result += 'DDO' + my_input[index + 6]
            index += 7
        else:
            result += 'NEVE' + my_input[index + 8]
            index += 9

    return result

        
def e(my_input):
    result = ''
    stack = []
    for index, i in enumerate(my_input):
        if i.isdigit():
            for j in stack[:]:
                result += stack.pop()
            result += i
        else:
            if my_input[index + 1].isdigit():
                stack.append(i.upper())
                continue
            stack.append(i.lower())

    return result


def f(my_input):
    result = ''
    numberlist = re.findall(r'\d+', my_input)
    for i in numberlist:
        result += i

    return result


if __name__ == '__main__':
    
    while True:
      number = input('Your number :')
      if not number.isdigit():
          print('please try again')
          continue
      break
    
    a = a(number)
    b = b(a)
    c = c(b)
    d = d(c)
    e = e(d)
    f = f(e)
    
    print('function a => ' + a)
    print('function b => ' + b)
    print('function c => ' + c)
    print('function d => ' + d)
    print('function e => ' + e)
    print('function f => ' + f)