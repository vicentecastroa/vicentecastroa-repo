# coding=utf-8

# Defina la clase 'Rational' en este espacio
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

    def mcm(self,other):
        menor = (self.fracion['den'],other.fracion['den'])
        for x in range(1,menor+1):
            if self.fracion['den']%x==0 and other.fracion['den']%x==0:
                mcm=x
        return mcm

    def suma(self,other):
        sum1=self.fracion['num']*other.fracion['den']
        sum2=other.fracion['num']*self.fracion['den']
        denominador= self.fracion['den']* other.fracion['den']
        suma=sum1+sum2
        return Rational(suma, denominador)

    def multiplicar(self,other):
        numerador=self.fracion['num']*other.fracion['num']
        denominador=self.fracion['den']*other.fracion['den']
        return Rational(numerador, denominador)

    def __add__(self, other):
        return (self.suma(self,other))

    def __sub__(self, other):
        return (self.suma(self,other))

    def __mul__(self, other):
        return self.multiplicar(self,other)

    def __truediv__(self, other):
        naux=other.fracion['den'] #doy vuelta la ea
        daux=other.fracion['num']
        other.fracion['num']=naux
        other.fracion['den']=daux
        return self.multiplicar(self,other)

    def __lt__(self, other): #menor
        a=self.fracion['num']*other.fracion['den']
        b=other.fracion['num']*self.fracion['den']
        if a<b:
            return True
        return False

    def __le__(self, other): #menorigual
        a=self.fracion['num']*other.fracion['den']
        b=other.fracion['num']*self.fracion['den']
        if a<=b:
            return True
        return False

    def __eq__(self, other): #igual
        if self.fracion['num']==other.fracion['num'] and self.fracion['den']==other.fracion['den']:
            return True
        return False

    def __ge__(self, other): #mayor igual
        a=self.fracion['num']*other.fracion['den']
        b=other.fracion['num']*self.fracion['den']
        if a>=b:
            return True
        return False

    def __gt__(self, other): #mayor
        a=self.fracion['num']*other.fracion['den']
        b=other.fracion['num']*self.fracion['den']
        if a>b:
            return True
        return False

    def __repr__(self):
        if self.fracion['den']==1:#si es entero
            return str(self.fracion['num'])
        return ("{}/{}".format(self.fracion['num'],self.fracion['den']))



if __name__ == "__main__":
    r1 = Rational(26, 4)
    r2 = Rational(-2, 6)
    r3 = Rational(34, 7)

    # 13/2 -1/3 34/7
    print(r1, r2, r3, sep=", ")

    # [Rational(1), Rational(-11/2)]
    print([Rational(1, 1), Rational(22, -4)])

    # 41/6
    print(r1 - r2)

    # 221/7
    print(r1 * r3)

    # 7/5
    print(r2 / Rational(5, -7))

    # True
    print(Rational(-4, 6) < Rational(1, -7))

    # True
    print(Rational(12, 8) == Rational(-24, -16))
