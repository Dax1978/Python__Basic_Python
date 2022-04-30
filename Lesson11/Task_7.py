####################################################################################################################
#                                                                                                                  #
# Задача 7                                                                                                         #
#                                                                                                                  #
####################################################################################################################

class Complex():
    def __init__(self, Re, Im) -> None:
        self.__Re = Re
        self.__Im = Im

    def get_Re(self):
        return self.__Re

    def set_Re(self, value):
        self.__Re = value

    Re = property(get_Re, set_Re)

    def get_Im(self):
        return self.__Im

    def set_Im(self, value):
        self.__Im = value

    Im = property(get_Im, set_Im)

    def __str__(self):
        cpx = str(self.__Re)
        if self.__Im >= 0:
            cpx += " + " + str(self.__Im) + "i"
        else:
            cpx += " - " + str(abs(self.__Im)) + "i"
        return cpx

    def __add__(self, other):
        return Complex(self.__Re + other.Re, self.__Im + other.Im)

    def __sub__(self, other):
        return Complex(self.__Re - other.Re, self.__Im - other.Im)

    def __mul__(self, other):
        return Complex(round(self.__Re * other.Re - self.__Im * other.Im, 2), round(self.__Im * other.Re + self.__Re * other.Im, 2))

    def __truediv__(self, other):
        return Complex(round((self.__Re * other.Re + self.__Im * other.Im)/(other.Re**2 + other.Im**2), 2), round((self.__Im * other.Re - self.__Re * other.Im) / (other.Re**2 + other.Im**2), 2))

    @property
    def __len__(self):
        return (self.__Re ** 2 + self.__Im ** 2) ** (0.5)


a = Complex(-10.0, -12.7)
b = Complex(7.7, 97.77)
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
print(a.__len__)
