def insertionsort(arr,i,n):
    if i==n:
        return
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
    insertionsort(arr,i+1,n)

arr=[13,46,36,22,1,7,90]
n=len(arr)

print("Before Using Insertion sort :")
print(arr)

insertionsort(arr,0,n)

print("After Using Insertion sort : ")
print(arr)

