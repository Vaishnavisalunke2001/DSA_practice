
class ArmstrongChecker:

    @staticmethod
    def is_armstrong(num):
        k = len(str(num))
        sum = 0
        n = num

        while n > 0:
            ld = n % 10             
            sum += ld ** k          
            n = n // 10             
        return sum == num

number = 153
if ArmstrongChecker.is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
