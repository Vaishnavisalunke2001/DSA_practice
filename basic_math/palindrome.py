def palindrome(n):
    revNo=0
    dup = n

    while n > 0:
        ld = n % 10
        revNo = revNo * 10 + ld
        n = n // 10

    return dup == revNo


number = 3445
if palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
