# 1> BRUTE FORCE SOLUTION - USING EMPTY SET
class solution :
    def removeduplicate_brute(self,nums):
        seen=set()
        index=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index]=num
                index+=1
        return index
    # TIME COMPLEXITY OF THIS SOLUTION IS : O(N)
    # SPACE COMPLEXITY OF THIS SOLUTION IS : O(N)

nums=[0,0,1,1,1,2,2,3,3,4]
sol=solution()
k1=sol.removeduplicate_brute(nums)
print("k = ",k1)
print("Array after removing dulpicates using brute force solution : ", nums[:k1])

# ---------------------------------------------------------------------------------------

# 2> OPTIMAL SOLUTION - USING TWO POINTERS
class Solution2:
    def removeduplicates_optimal(self,nums):
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
    # TIME COMPLEXITY OF THIS SOLUTION IS : O(N)
    # SPACE COMPLEXITY OF THIS SOLUTION IS : O(1)

nums=[0,0,1,1,1,2,2,3,3,4]
sol=Solution2()
k2=sol.removeduplicates_optimal(nums)
print("k2 = ",k2)
print("Array after removing dulpicates using optimal solution : ", nums[:k2])


