# Iterative Implementation
class Solution:
    def binarysearch(self,nums:[int],target:int)->int:
        n=len(nums)
        low=0
        high=n-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
    
if __name__=="__main__":
    a=[3,4,6,7,9,12,36,54,85]
    target=36

    obj=Solution()
    ind=obj.binarysearch(a,target)

    if ind==-1:
        print("The target is not present.")
    else:
        print("The target is at index: ",ind)

# -----------------------------------------------------
# Recursive approch

class Solution1:
    def binarysearch1(self,nums:[int],low:int,high:int,target:int)->int:
        if low>high:
            return -1
        
        mid=(low+high)//2

        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            return self.binarysearch1(nums,mid+1,high,target)
        else:
            return self.binarysearch1(nums,low,mid-1,target)
        
    def search(self,nums:[int],target:int)->int:
        return self.binarysearch1(nums,0,len(nums)-1,target)
    
if __name__=="__main__":
    a=[3,4,5,9,12,32,41,52,63,74]
    target=9
    obj1=Solution1()
    ind=obj1.search(a,target)

    if ind==-1:
        print("The target is not present.")
    else:
        print("The target is at index: ",ind)


    
    

