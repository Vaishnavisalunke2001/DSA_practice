# 1> BRUTE FORCE SOLUTION
def solve(arr,n):
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=arr[i]
    temp[n-1]=arr[0]
    for num in temp:
        print(num,end=" ")
    print()

if __name__=="__main__":
    n=5
    arr=[1,2,3,4,5]
    solve(arr,n)
    # TIME COMPLEXITY OF THIS SOLUTION IS : O(N)
    # SPACE COMPLEXITY OF THIS SOLUTION IS : O(N)

# 2> OPTIMAL SOLUTION
class Solution:
    def rotateArrayByOne(self,nums):
        temp=nums[0]
        for i in range(1,len(nums)):
            nums[i-1]=nums[i]
        nums[-1]=temp
if __name__=="__main__":
    sol=Solution()
    nums=[1,2,3,4,5]
    sol.rotateArrayByOne(nums)
    print("rotate array by one using optimal solution : ",nums)

    # TIME COMPLEXITY OF THIS SOLUTION IS : O(N)
    # SPACE COMPLEXITY OF THIS SOLUTION IS : O(1)
