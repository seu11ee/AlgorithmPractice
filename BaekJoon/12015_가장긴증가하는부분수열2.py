#dp
#binary search

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

def binarySearch(k,l):
    start = 0
    end = len(l)-1
    mid = (start + end) // 2
    while(start<end):
        if l[mid] > k :
            return l[mid]

        else:
start = 0
end = len(a)-1
mid = (start + end)//2
stack = [0]
while(start<end):
    if a[mid] > max(stack):
        stack.append(a[mid])
