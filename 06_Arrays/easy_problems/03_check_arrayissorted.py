# 1> BRUTE FORCE SOLUTION
def issorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                return False
    return True
arr=[1,2,3,4,5]
n=len(arr)
print("brute force solution is : ")
ans=issorted(arr,n)
if ans:
    print("True")
else:
    print("False")

# TIME COMPLEXITY OF THIS SOLUTION IS : O(N^2)
# SPACE COMPLEXITY OF THIS SOLUTION IS : O(1)

# -------------------------------------------------------------------
# 2> OPTIMAL SOLUTION
def issorted(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True
arr=[1,2,3,4,5]
n=len(arr)
print("optimal solution is : ")
print("True" if issorted(arr,n) else "False")

# TIME COMPLEXITY OF THIS SOLUTION IS : O(N)
# SPACE COMPLEXITY OF THIS SOLUTION IS : O(1)
