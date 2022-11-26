class Rational_Numbers:
    def __init__(self, numerator, denominator):
        # checking whether the numerator and denominator values are integers or not, if not then raising error!
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError("The numerator and denominator of a fraction must be an integer!")
        # denominator must not be zero!
        if denominator == 0:
            raise ZeroDivisionError("The Denominator of a Fraction can't be Zero")

        # if numerator is zero then represent in form... 0/1
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        # if numerator not zero then checking the sign of our number...
        else:
            if ((numerator<0 and denominator>0) or (numerator>0 and denominator<0)):
                sign = -1
            else:
                sign = 1
            (self._numerator, self._denominator) = self._reduce(numerator, denominator, sign)
            print((self._numerator), "/" ,(self._denominator))

    # <-----------now let's reduce our fraction to the lowest form-------------->
    # declaring the private method...
    def _reduce(self, n, d, sign):      # taking ex. n = -9 and d = 18
        a = abs(n)      # converting -ve number to +ve using the abs() function
        b = abs(d)
        # <---------- logic for reducing our fraction ----------->
        while a % b != 0:       # a = 9 and b = 18
            tempA = a           # tempA = 9
            tempB = b           # tempB = 18
            a = tempB           # a = 18
            b = tempA % tempB   # b = 9 % 18 => 9

        ret_n = abs(n) // b * sign      # ret_n = 9 // 9 * -1 ----> (-1)
        ret_d = abs(d) // b             # ret_d = 18 // 9     ---->  2
        return ret_n, ret_d
        # <---------- over ---------->


    # Arithmetic Operations...
    # Add Operation...
    def add(self, a, b, c, d):
        num = a * d + c * b
        deno = b * d
        # print(str(Rational_Numbers(num,deno)))
        # print("Addition is: ", str(num), "/", str(deno))
        return Rational_Numbers(num, deno)

    # Sub Operation
    def sub(self, a, b, c, d):
        num = a * d - c * b
        deno = b * d
        # print(str(Rational_Numbers(num, deno)))
        # print("Subtraction is: ", str(num), "/", str(deno))
        return Rational_Numbers(num, deno)

    # Mul Operation
    def mul(self, a, b, c, d):
        num = a * c
        deno = b * d
        # print(Rational_Numbers(num, deno))
        # print("Multiplication is: ", str(num), "/", str(deno))
        return Rational_Numbers(num, deno)

    # Div Operation
    def div(self, a, b, c, d):
        num = a * d
        deno = b * c
        # print(Rational_Numbers(num, deno))
        # print("Division is: ", str(num), "/", str(deno))
        return Rational_Numbers(num, deno)

# Driver Code...
obj = Rational_Numbers(-9, 18)
print("Addition in Reduced (p/q) form is:", end=" "), obj.add(1, 2, 3, 4)
print("Subtraction in Reduced (p/q) form is:", end=" "), obj.sub(1, 2, 3, 4)
print("Multiplication in Reduced (p/q) form is:", end=" "), obj.mul(1, 2, 3, 4)
print("Division in Reduced (p/q) form is: ", end=" "), obj.div(1, 2, 3, 4)


# There's a Module named fraction in python which also does the same work as above

