from collections import defaultdict

class Solution:
    def Frequency(self,arr,n):
        Freq_map=defaultdict(int)

        for i in range(n):
            Freq_map[arr[i]]+=1

        for key,value in Freq_map.items():
            print(key,"-",value)

if __name__=="__main__":
    arr=[10,5,10,15,10,5]
    n=len(arr)
    sol=Solution()
    sol.Frequency(arr,n)