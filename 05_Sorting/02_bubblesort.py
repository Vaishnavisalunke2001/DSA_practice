class Bubblesort:
    def Bubble_sort(self,arr):
        n=len(arr)

        for i in range(n-1,-1,-1):
            did_swap=False

            for j in range(i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    did_swap=True
            if not did_swap:
                break

        print("After using bubble sort : ")
        print(" ".join(map(str,arr)))

if __name__ == "__main__":
    arr=[13,45,67,3,98,32]
    print("Before using bubble sort : ")
    print(" ".join(map(str,arr)))

    sorter = Bubblesort()
    sorter.Bubble_sort(arr)