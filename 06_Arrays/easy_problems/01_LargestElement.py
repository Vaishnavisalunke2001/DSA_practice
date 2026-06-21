def LargestElement(arr,n):
    largest=arr[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest=arr[i]
    return largest

if __name__=='__main__':
    arr=[2,78,90,46,38,21,3]
    n=len(arr)
    max=LargestElement(arr,n)
    print("Largest Element is : ",max)


