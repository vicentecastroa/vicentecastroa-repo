__author__ = 'Vicente'

class Rational():
    def __init__(self, num, den):
        self.fracion={'num':num,'den':den}
        self.menor=min(num, den)
        self.mayor=max(num, den)

        for x in range(1, abs(self.menor)+1):
            if self.fracion['num']%x==0 and self.fracion['den']%x==0: #simplifica ambos numeros
                self.fracion['num']=self.fracion['num']//x
                self.fracion['den']=self.fracion['den']//x
        if self.fracion['num']*self.fracion['den']>0: #si los dos son negativos
            self.fracion['num']=abs(self.fracion['num'])
            self.fracion['den']=abs(self.fracion['den'])
        if self.fracion['num']>0 and self.fracion['den']<0: #si el signo - esta en el denominador
            self.fracion['num']=-self.fracion['num']
            self.fracion['den']=abs(self.fracion['den'])

    def __repr__(self):
        if self.fracion['den']==1:#si es entero
            return str(self.fracion['num'])
        return ("{}/{}".format(self.fracion['num'],self.fracion['den']))

print(Rational(24,10))
print(Rational(40,10))
print(Rational(2,-10))
print(Rational(2,6))
print(Rational(-5,-2))

