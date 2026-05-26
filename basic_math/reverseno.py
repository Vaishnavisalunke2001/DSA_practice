class Solution:
    def reverseno(self,n):
        revNo=0
        while(n>0):
            lastNo = n % 10
            revNo=revNo*10+lastNo
            n=n//10
        return revNo


obj=Solution()
num=12345
print("N", num )
Rev_No=obj.reverseno(num)
print("Reverse of no : ",Rev_No)

