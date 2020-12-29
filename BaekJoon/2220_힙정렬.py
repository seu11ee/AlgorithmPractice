import sys
from itertools import permutations

n = int(sys.stdin.readline())
max = 0
cnt = 0
answer = []
heapSize = 0
def maxHeapify(a,i):
    global cnt
    global heapSize
    l = 2*i + 1
    r = 2*i + 2
    if l < heapSize and a[i] < a[l]:
        largest = l
    else:
        largest = i
    if r < heapSize and a[largest] < a[r]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        cnt += 1
        # print(a)
        # print("cnt",cnt,a)
        maxHeapify(a,largest)

def buildMaxHeap(a):
    k = heapSize
    for i in range(k//2-1,-1,-1):
        maxHeapify(a,i)
    return a
def heapSort(a):
    global heapSize
    global cnt
    heapSize = len(a)
    cnt = 0
    buildMaxHeap(a)
    for i in range(len(a),1,-1):
        a[0],a[i-1] = a[i-1],a[0]
        heapSize -= 1
        maxHeapify(a,0)



for l in permutations(range(1,n+1),n):
    temp = list(l)

    heapSort(temp)
    if cnt > max:
        max = cnt
        answer.append(l)

for i in answer:
    print(i,end = " ")

