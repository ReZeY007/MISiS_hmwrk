from math import gcd

class Rational:

    def __init__ (self, num, denum):
        if denum == 0:
            raise ValueError("Zero division")
        elif denum < 0:
            self.num = -num
            self.denum = -denum
        else:
            self.num = num
            self.denum = denum
        

    @staticmethod
    def reduct(rat):
        num = rat.num
        denum = rat.denum
        nod = gcd(num, denum)

        num //= nod
        denum //= nod

        return Rational(num, denum)


    def __str__(self):
        if self.num == 0:
            return "0"
        # elif self.num % self.denum == 0:
        #     return str(self.num // self.denum)
        else:
            return f"{str(self.num)}/{str(self.denum)}"
    

    def __mul__(self, other):
        if type(other) == Rational:
            return Rational.reduct(Rational(self.num * other.num, self.denum * other.denum))
        elif type(other) == int:
            return Rational.reduct(Rational(self.num * other, self.denum))
    

    def __add__(self, other):
        if type(other) == Rational:
            denum = self.denum * other.denum
            num1 = self.num * other.denum
            num2 = other.num * self.denum
            num = num1 + num2

            return Rational.reduct(Rational(num, denum))
        elif type(other) == int:
            return Rational.reduct(Rational(self.num + other * self.denum, self.denum))


    def __sub__(self, other):
        if type(other) == Rational:
            denum = self.denum * other.denum
            num = self.num * other.denum - other.num * self.denum

            return Rational.reduct(Rational(num, denum))
        elif type(other) == int:
            return Rational.reduct(Rational(self.num - other * self.denum, self.denum))
    

    def __truediv__(self, other):
        if type(other) == Rational:
            if other.num == 0:
                raise ValueError("Zero division")

            num = self.num * other.denum
            denum = self.denum * other.num

            return Rational.reduct(Rational(num, denum))
        elif type(other) == int:
            if other == 0:
                raise ValueError("Zero division")

            return Rational.reduct(Rational(self.num, self.denum * other))            


    def __eq__(self, other):
        if type(other) == Rational:
            num1 = self.num * other.denum
            num2 = self.denum * other.num

            if num1 == num2: return True    
            else: return False
        elif type(other) == int:
            if self.num == other * self.denum: return True
            else: return False

    def __gt__(self, other):
        if type(other) == Rational:
            num1 = self.num * other.denum
            num2 = self.denum * other.num

            if num1 > num2: return True
            else: return False
        elif type(other) == int:
            if self.num > other * self.denum: return True
            else: return False
            

    def __lt__(self, other):
        if type(other) == Rational:
            num1 = self.num * other.denum
            num2 = self.denum * other.num

            if num1 < num2: return True
            else: return False 
        elif type(other) == int:
            if self.num < other * self.denum: return True
            else: return False


    def __ge__(self, other):
        if type(other) == Rational:
            num1 = self.num * other.denum
            num2 = self.denum * other.num

            if num1 >= num2: return True
            else: return False
        elif type(other) == int:
            if self.num >= other * self.denum: return True
            else: return False


    def __le__(self, other):
        if type(other) == Rational:
            num1 = self.num * other.denum
            num2 = self.denum * other.num

            if num1 <= num2: return True
            else: return False
        elif type(other) == int:
            if self.num < other * self.denum: return True
            else: return False

    def __neg__(self):
        num = -self.num

        return Rational.reduct(Rational(num, self.denum)) 



cl1 = Rational(5, 5)
cl2 = Rational(5, 5)
print(cl1 >= 0)