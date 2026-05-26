import math
def countdigit(n):          #O(log10(n))
    cnt=(int)(math.log10(n)+1)
    return cnt

def countdigits2(n):        #O(1)
    cnt=0
    while (n>0):
        cnt=cnt+1
        n=n//10
    return cnt

if __name__=="__main__":
    n = 1234 
    print("N", n)
    digits=countdigit(n)
    digits2=countdigits2(n)
    print("count of digits : ", digits)
    print("count of digits2 : ", digits2)

