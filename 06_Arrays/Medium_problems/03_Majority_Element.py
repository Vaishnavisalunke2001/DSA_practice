# find majority element that occurs more than n/2 times
# 1> brute force approch
from typing import List
class Solution:
    def majorityElement(self,arr: List[int])->int:
        n=len(arr)
        for i in range(n):
            cnt=0
            for j in range(n):
                if arr[j]==arr[i]:
                    cnt+=1
            if cnt>(n//2):
                return arr[i]
        return -1

if __name__=="__main__":
    arr=[2,2,1,1,1,2,2]
    sol=Solution()
    ans=sol.majorityElement(arr)
    print("The majority element is : ",ans)

# ----------------------------------------------

# 2> Better solution (using hashing)
class Solution2:
    def majorelement(self,arr: List[int])->int:
        n=len(arr)
        mp={}
        for num in arr:
            if num in mp:
                mp[num]+=1
            else:
                mp[num]=1
            
        for num,count in mp.items():
            if count>n//2:
                return num
        return -1

if __name__=="__main__":
    arr=[2,2,1,1,2,2,2,3,3]
    sol2=Solution2()
    ans=sol2.majorelement(arr)
    print("The majority element is:", ans)

# -----------------------------------------------------

# 3> optimal solution
class Solution3:
    def majorElements(self,arr: List[int])->int:
        n=len(arr)
        cnt=0
        ele=0
        for num in arr:
            if cnt==0:
                cnt=1
                ele=num
            elif ele==num:
                cnt+=1
            else:
                cnt-=1
        cnt1=arr.count(ele)

        if cnt1>(n//2):
            return ele
        return -1
    
arr=[2,2,1,1,1,2,2]
sol3=Solution3()
ans=sol3.majorElements(arr)
print(f"The majority element is: {ans}")