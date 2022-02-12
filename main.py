import re


def a(number):
    snumber = str(number)
    result = ''
    for i in snumber:
        if int(i) % 2 == 0:
            result += 'Even' + i
        else:
            result += 'Odd' + i

    return result


def b(my_input):
    return my_input.replace('Odd', 'DDO').replace('Even', 'NEVE')


def c(my_input):
    return my_input.replace('DDO', '686879').replace('NEVE', '78698669')


def d(my_input):
    return my_input.replace('686879', 'DDO').replace('78698669', 'NEVE')


def e(my_input):
    return my_input.replace('DDO', 'Odd').replace('NEVE', 'Even')


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
