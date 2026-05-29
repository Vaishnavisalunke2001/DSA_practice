class Solution:
    def PrintNo(self,current):
        if current < 1 :
            return
        print(current , end=" ")
        self.PrintNo(current-1)

if __name__ == "__main__":
    sol = Solution()
    n = 10
    sol.PrintNo(n)
    print()
