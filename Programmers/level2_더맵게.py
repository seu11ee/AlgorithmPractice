''' Heapq이용 자료구조에서 힙 찾아보깅'''
from heapq import *

def solution(scoville, K):
    heapify(scoville)
    count=0
    while(scoville[0]<K):
        if len(scoville)<2:
            return -1
        count+=1
        a = heappop(scoville)

        b = heappop(scoville)
        if b==-1:
            return -1
        heappush(scoville,a+2*b)
    return count
