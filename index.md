## ODDS Assignments

<iframe src="https://trinket.io/embed/python/0e97d353f7?runOption=run" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

```python
import re

class OddnEven:

    def __init__(self, odd_prefix, even_prefix):

        self.ODD_PREFIX = odd_prefix
        self.EVEN_PREFIX = even_prefix

        self.ODD_ASCII = ''
        self.EVEN_ASCII = ''

        ascii_list = [ord(character) for character in self.ODD_PREFIX[::-1].upper()]
        for c in ascii_list:
            self.ODD_ASCII += str(c)

        ascii_list = [ord(character) for character in self.EVEN_PREFIX[::-1].upper()]
        for c in ascii_list:
            self.EVEN_ASCII += str(c)


    def a(self, number):
        snumber = str(number)
        result = ''
        for i in snumber:
            if int(i) % 2 == 0:
                result += self.EVEN_PREFIX + i
            else:
                result += self.ODD_PREFIX + i

        return result


    def b(self, my_input):
        return my_input.replace(self.ODD_PREFIX, self.ODD_PREFIX[::-1].upper()).replace(self.EVEN_PREFIX, self.EVEN_PREFIX[::-1].upper())


    def c(self, my_input):
        return my_input.replace(self.ODD_PREFIX[::-1].upper(), self.ODD_ASCII).replace(self.EVEN_PREFIX[::-1].upper(), self.EVEN_ASCII)


    def d(self, my_input):
        return my_input.replace(self.ODD_ASCII, self.ODD_PREFIX[::-1].upper()).replace(self.EVEN_ASCII, self.EVEN_PREFIX[::-1].upper())


    def e(self, my_input):
        return my_input.replace(self.ODD_PREFIX[::-1].upper(), self.ODD_PREFIX).replace(self.EVEN_PREFIX[::-1].upper(), self.EVEN_PREFIX)


    def f(self, my_input):
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

    oddnEven = OddnEven('Odd', 'Even')

    a = oddnEven.a(number)
    b = oddnEven.b(a)
    c = oddnEven.c(b)
    d = oddnEven.d(c)
    e = oddnEven.e(d)
    f = oddnEven.f(e)

    print('function a => ' + a)
    print('function b => ' + b)
    print('function c => ' + c)
    print('function d => ' + d)
    print('function e => ' + e)
    print('function f => ' + f)
```

