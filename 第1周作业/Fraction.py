from typing import List


def gcd(m, n):
    while m % n != 0:
        m, n = n, m%n
    return n


class Fraction:
    def __init__(self, top, bottom): #定义函数
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common_divisor = gcd(new_num, new_den)
        return Fraction(new_num//common_divisor, new_den//common_divisor)


input1 = list(map(int, input().split()))

Fraction1 = Fraction(input1[0], input1[1])
Fraction2 = Fraction(input1[2], input1[3])

print(Fraction1 + Fraction2)
