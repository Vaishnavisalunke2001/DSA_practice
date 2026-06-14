def bubblesort(arr,n):
    if n==1:
        return
    did_swap=False
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            did_swap=True

    if not did_swap:
        return
    bubblesort(arr,n-1)

arr=[13,56,43,89,21,5]
print("Before Using Bubble sort : ")
print(arr)

bubblesort(arr,len(arr))

print("After Using Bubble sort : ")
print(arr)
