def isPrime(N):
    cnt = 0
    for i in range(1, N + 1):
        if (N % i == 0):
            cnt += 1
    return cnt == 2

N = 1483
CheckPrime = isPrime(N)
if CheckPrime:
    print(f"{N} is a prime")
else:
    print(f"{N} is not a prime")

