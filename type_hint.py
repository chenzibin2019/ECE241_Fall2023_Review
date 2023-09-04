import math
class Fraction:
    def __init__(self, num: int, den: int):
        """
        Constructor: takes numerator and denominator as input
        :param num: The numerator
        :param den: The denominator
        """
        self.num: int = num
        self.den: int = den

    def __str__(self):
        """
        Override the default __str__ function
        :return: None
        """
        return str(self.num) + "/" + str(self.den)

    def add(self, rhs: "Fraction"):
        """
        Add the fraction with another fraction (rhs)
        :param rhs: The right-hand-side
        :return: The resulting fraction
        """
        lcm: int = math.lcm(self.den, rhs.den)  # lease common multiple
        num1: int = int(self.num * lcm / self.den)  # numerator for the first fraction after scaling to lcm
        num2: int = int(rhs.num * lcm / rhs.den)    # numerator for the second fraction after scaling to lcm
        return Fraction(num1 + num2, lcm)


# half = Fraction(1, 2)
# quarter = Fraction(1, 4)
# print(half.add(quarter))

# Type hint does not prevent you from messing up the variables, so be careful
# half.num = "wow"
# print(half)

