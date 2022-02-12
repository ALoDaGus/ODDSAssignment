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
    return param.replace('Odd', 'DDO').replace('Even', 'NEVE')


def c(param):
    return param.replace('DDO', '686879').replace('NEVE', '78698669')


def d(param):
    return param.replace('686879', 'DDO').replace('78698669', 'NEVE')


def e(param):
    return param.replace('DDO', 'Odd').replace('NEVE', 'Even')


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
