
class kasr:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator


    def sum(self, x):
        result = kasr(None, None)
        result.num = x.num * self.den + x.den * self.den
        result.den = x.den * self.den
        return result


    def sub(self, x):
        result = kasr(None, None)
        result.num = x.num * self.den - x.den * self.den
        result.den = x.den * self.den
        return result


    def mul(self, x):
        result = kasr(None, None)
        result.num = x.num * self.num
        result.den = x.den * self.den
        return result


    def div(self, x):
        result = kasr(None, None)
        result.num = x.num / self.num
        result.den = x.den / self.den
        return result

    def show(self):
        print( self.num, '/', self.den )

print('fisrt fraction:')        
a = kasr( int(input('enter the fisrt numerator: ')), int(input('enter the fisrt denominator: ')) )     
print('second fraction:')
b = kasr( int(input('enter the second numerator: ')), int(input('enter the  second denominator: ')) )     

sum = a.sum(b)
sub = a.sub(b)
mul = a.mul(b)
div = a.div(b)

print('sum : ', end='')
sum.show()

print('sub : ' , end='')
sub.show()

print('mul : ' , end='')
mul.show()

print('div : ' , end='')
div.show()