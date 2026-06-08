class FrequencyCounter:
    def countFreq(self,arr):
        n=len(arr)
        visited=[False]*n
        maxFreq=0
        minFreq=n
        maxEle=0
        minEle=0

        for i in range(n):
            if visited[i]:
                continue

            count=1
            for j in range(i+1,n):
                if arr[i]==arr[j]:
                    visited[j]=True
                    count+=1
                
            if count>maxFreq:
                maxEle=arr[i]
                maxFreq=count

            if count<minFreq:
                minEle=arr[i]
                minFreq=count

        print("The Highest frequency element is : ",maxEle)
        print("The Lowest frequency element is : ",minEle)

if __name__=="__main__":
    arr=[10,5,10,15,10,5]
    fc = FrequencyCounter()
    fc.countFreq(arr)
