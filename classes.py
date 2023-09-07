
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
        print(self.num, "/", self.den)

    def toDecimal(self):
        return self.num / self.den

half = Fraction(1, 2)
print(half)
half.show()
print(half.toDecimal())

quarter = Fraction(1, 4)
print(quarter)
quarter.show()
print(quarter.toDecimal())
