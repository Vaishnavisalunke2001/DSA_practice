class Solution:
    def PrintNo(self,current,n):
        if (current > n):
            return
        print(current,end=" ")
        self.PrintNo(current+1,n)

if __name__ == "__main__":
    sol = Solution()
    n=10
    sol.PrintNo(1,n)
    print()

    