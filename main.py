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


def b(param):
    param = param.replace('Odd', 'DDO')
    param = param.replace('Even', 'NEVE')
    return param


def c(param):
    param = param.replace('DDO', '686879')
    param = param.replace('NEVE', '78698669')
    return param


def d(param):
    param = param.replace('686879', 'DDO')
    param = param.replace('78698669', 'NEVE')
    return param

        
def e(param):
    param = param.replace('DDO', 'Odd')
    param = param.replace('NEVE', 'Even')
    return param


def f(param):
    result = ''
    numberlist = re.findall(r'\d+', param)
    for i in numberlist:
        result += i

    return result


if __name__ == '__main__':
    number = input('Your number :')
    print('function a => ' + a(number))
    print('function b => ' + b(a(number)))
    print('function c => ' + c(b(a(number))))
    print('function d => ' + d(c(b(a(number)))))
    print('function e => ' + e(d(c(b(a(number))))))
    print('function f => ' + f(e(d(c(b(a(number)))))))