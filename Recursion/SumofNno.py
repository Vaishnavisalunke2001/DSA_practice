class Solution:
    def SumofNaturalNo(self,n):
        if n==0:
            return 1
        return n+self.SumofNaturalNo(n - 1)
    
if __name__ == "__main__":
    obj = Solution()
    n = 3
    sum = obj.SumofNaturalNo(n)
    print("Sum of Natual No : ", sum)

