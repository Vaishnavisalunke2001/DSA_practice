class Solution:
    def quicksort(self,arr,low,high):
        if low<high:
            pivotindex=self.partition(arr,low,high)
            self.quicksort(arr,low,pivotindex-1)
            self.quicksort(arr,pivotindex+1,high)

    def partition(self,arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
# arr =[10,7,8,9,1,5]
n = int(input("Enter size: "))
arr=list(map(int,input("Input array : ").split(',')))
sol=Solution()
sol.quicksort(arr,0,len(arr)-1)
print(*arr)

