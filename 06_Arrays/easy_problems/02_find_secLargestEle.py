class Solution:
    def secLargestEle(arr,n):
        largest='-inif'
        seclargest='-inif'

        for i in range(1,n):
            if arr[i]>largest:
                seclargest=largest
                largest=arr[i]

            elif arr[i]>seclargest and arr[i]==largest:
                seclargest=arr[i]