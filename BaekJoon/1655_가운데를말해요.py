# import sys
# import heapq
# from collections import deque
#
# n = int(sys.stdin.readline())
# heap1 = list()
# stack = list()
# for cnt in range(n):
#     heapq.heappush(heap1,int(sys.stdin.readline()))
#     #print(heap1)
#     stack = []
#     for _ in range(cnt//2+1):
#         stack.append(heapq.heappop(heap1))
#
#     print(stack[-1])
#     heap1+=stack
#     heapq.heapify(heap1)

import sys
import heapq

n = int(input())
heap = []
for cnt in range(n):
    heapq.heappush(heap,int(input()))
    print(heap)