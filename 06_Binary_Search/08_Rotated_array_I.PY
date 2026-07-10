# Brute force approch
class Solution:
    def search(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

nums=[4,5,6,7,0,1,2]
target=0
obj=Solution()
index=obj.search(nums,target)

print(index)

# -------------------------------------------------------
# Opimal Solution 
class Solution1:
    def search(self,nums,target):
        low=0
        high=len(nums)-1

        while(low<=high):
            mid=(low+high)//2

            if nums[mid]==target:
                return mid
            
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

nums=[4,5,6,7,0,1,2]
target=1
obj1=Solution1()
result1=obj1.search(nums,target)
print(result1)


