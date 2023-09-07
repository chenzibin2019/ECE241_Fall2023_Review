
class Fraction:

    def __init__(self, num, den):
        """
        Constructor: Takes the number and denominator as input
        :param num: The numerator
        :param den: The denominator
        """
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)  # Return, not print!!!

    def show(self):
        """
        Print the fraction
        :return: None
        """
        print(self.num, "/", self.num)

    def toDecimal(self):
        return self.num / self.den


frac = Fraction(1, 6)
print(frac)
frac.show()
print(frac.toDecimal())
