import sys
n = int(sys.stdin.readline().rstrip())
products = list(map(int,sys.stdin.readline().rstrip().split(" ")))
products.sort()
m = int(sys.stdin.readline().rstrip())
orders = list(map(int,sys.stdin.readline().rstrip().split(" ")))
def binarySearch(n,l,r):
    if l > r:
        return "no"
    m = (l+r)//2
    mid = products[m]
    if mid == n:
        return "yes"
    if n < mid:
        return binarySearch(n,l,m-1)
    else:
        return binarySearch(n,m+1,r)

for order in orders:
    print(binarySearch(order,0,n-1),end = " ")
