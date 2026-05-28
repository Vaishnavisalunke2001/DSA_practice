class Divisors:
    def GetDivisors(self, N):
        res = []
        for i in range(1,N + 1):
            if N % i == 0:
                res.append(i)
        return res

sol = Divisors()
N = 36
result = sol.GetDivisors(N)
print("Divisors of ",N,"=",*result)

