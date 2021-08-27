import sys

def binary_search(arr,l,r):
    minimum_sum = int(1e9)*2
    return_val = arr[l],arr[r]
    while l<r :
        if arr[l]+arr[r] == 0:
            return arr[l],arr[r]
        if abs(arr[l]+arr[r]) < minimum_sum:
            minimum_sum = abs(arr[l]+arr[r])
            return_val = arr[l],arr[r]
        elif arr[l]+arr[r] > 0:
            r -= 1
        else:
            l += 1
    return return_val

input = sys.stdin.readline
n = int(input())
liquids = list(map(int,input().split()))
liquids.sort()
a,b = binary_search(liquids,0,len(liquids)-1)

print(a,b)


