__author__ = 'Vicente'

class Audifono:
    def __init__(self, impedancia='', rangofrec='', intensidadmax=''):
        self.impedancia = impedancia
        self.rangofrecuencia = rangofrec
        self.intensidadmax = intensidadmax


    def escuchar(self, cancion):
        print("la cancion "+cancion+" esta siendo reproducida desde un audifono")



class OverEar(Audifono):
    def __init__(self, aislacion='', **kwargs):
        super().__init__(**kwargs)
        self.aislacion = aislacion

class Intraaural(Audifono):
    def __init__(self, comodidad='', **kwargs):
        super().__init__(**kwargs)
        self.comodidad = comodidad

class Inalambrico(Audifono):
    def __init__(self, rangomax='', **kwargs):
        super().__init__(**kwargs)
        self.rangomax = rangomax

    def escuchar(self, cancion):
        print("la cancion "+cancion+" esta siendo reproducida desde un audifono inalambrico")

class Bluetooth(Inalambrico,Audifono):
    def __init__(self,bluetooth='',**kwargs):
        super().__init__(**kwargs)
        self.bluetooth=bluetooth


    def escuchar(self, cancion):
        print("la cancion "+cancion+" esta siendo reproducida desde un audifono con bluetoth")



audifono1 = OverEar(aislacion='100', impedancia='20',rangofrec='10,50', intensidadmax='-20')
audifono2 = Inalambrico(rangomax='15', impedancia='15', rangofrec='15,60', intensidadmax='-30')
audifono3 = Bluetooth(bluetooth='si', rangomax='20', impedancia='30', rangofrec='0,60', intensidadmax='-5')

audifono1.escuchar('alive')
audifono2.escuchar('black')
audifono3.escuchar('thunderstrack')










