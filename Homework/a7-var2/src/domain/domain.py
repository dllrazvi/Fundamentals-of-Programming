class Complex:
    def __init__(self, real:int, imag:int):
        assert type(real)==int and type(real)==int,str(real)+'/'+str(real)+'not integers'
        self.__real= real
        self.__imag= imag

    @property
    def real(self):
        return self.__real

    @property
    def imag(self):
        return self.__imag

    def __str__(self):
        if self.__imag>=0:
            return str(self.__real)+'+'+str(self.__imag)+'i'
        else:
            return str(self.__real) + str(self.__imag) + 'i'