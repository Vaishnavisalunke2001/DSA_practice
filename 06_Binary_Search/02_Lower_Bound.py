# Brute force approch
class lowerboundfinder:
    def lower_bound(self,arr,x):
        for i in range(len(arr)):
            if arr[i]>=x:
                return i
        return len(arr)

arr=[3,5,8,9,15]
x=10

finder=lowerboundfinder()
ind=finder.lower_bound(arr,x)

print("The lower bound is the index: ", ind)

# ----------------------------------------------------
# Optimal Solution
class lowerboundfinder1:
    def lower_bound1(self,arr,x):
        low,high=0,len(arr)-1
        ans=len(arr)

        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

arr=[3,5,8,9,15]
x=10

finder=lowerboundfinder1()
ind=finder.lower_bound1(arr,x)

print("The lower bound is the index: ", ind)