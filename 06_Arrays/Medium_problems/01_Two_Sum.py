# 1> BRUTE FORCE APPROCH
class Solution:
    def two_sum_exist(self,arr,target):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==target:
                    return "YES"
        return "NO"
    def two_sum_indices(self,arr,target):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==target:
                    return [i,j]
        return [-1,-1]

if __name__=="__main__":
    sol=Solution()
    arr=[2,6,5,8,11]
    target=14
    # variant 1
    print(sol.two_sum_exist(arr,target))
    # variant 2
    print(sol.two_sum_indices(arr,target))

# --------------------------------------------------------------
# 2> better solution using hashing

class Solution2:
    # variant 1
    def two_sum_exists(self,arr,target):
        mp={}
        for i, num in enumerate(arr):
            complement=target-num
            if complement in mp:
                return "YES"
            mp[num]=i
        return "NO"

    # variant 2
    def two_sum_indice(self,arr,target):
        mp={}
        for i, num in enumerate(arr):
            complement=target-num
            if complement in mp:
                return [mp[complement],i]
            mp[num]=i
        return [-1,-1]
    
if __name__=="__main__":
    sol2=Solution2()
    arr=[2,6,5,8,11]
    target=14
    print(sol2.two_sum_exists(arr, target))
    print(sol2.two_sum_indice(arr, target))

# -----------------------------------------------------------
# 3> optimal solution using 2 pointers greedy approch

class Solution3:
    def two_sum_exists(self,arr,target):
        nums_with_index=[(num,idx) for idx,num in enumerate(arr)]
        nums_with_index.sort(key=lambda x:x[0])

        left,right=0,len(arr)-1

        while left<right:
            current_sum=nums_with_index[left][0]+nums_with_index[right][0]

            if current_sum==target:
                return "YES"
            elif current_sum<target:
                left+=1
            else:
                right-=1
        return "NO"
    
    def two_sum_indices(self,arr,target):
        nums_with_index=[(num,idx) for idx, num in enumerate(arr)]

        nums_with_index.sort(key=lambda x: x[0])
        left,right=0,len(arr)-1

        while left<right:
            current_sum=nums_with_index[left][0]+nums_with_index[right][0]

            if current_sum==target:
                return [nums_with_index[left][1],nums_with_index[right][1]]
            elif current_sum<target:
                left+=1
            else:
                right-=1
        return [-1,-1]
if __name__=="__main__":
    sol3=Solution3()
    arr=[2,6,5,8,11]
    target=14
    print(sol3.two_sum_exists(arr, target))  # Output: YES
    print(sol3.two_sum_indices(arr, target)) # Output: [1, 3]

