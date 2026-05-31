class Solution:
    def FactofNo(self,n):
        if n == 0:
            return 1
        return n * self.FactofNo(n-1)
    
if __name__ == "__main__":
    obj=Solution()
    n=int(input())
    factno = obj.FactofNo(n)
    print("factorial of no : ", factno)
    
    