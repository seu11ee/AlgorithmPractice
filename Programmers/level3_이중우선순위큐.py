import heapq

def solution(operations):
    answer = []
    maxHeap = []
    minHeap = []
    for op in operations:
        order, data = op.split(" ")
        data = int(data)
        if order == "I":
            heapq.heappush(maxHeap,(-data,data))
            heapq.heappush(minHeap,(data,data))
        else:
            if data == 1:
                if len(maxHeap) == 0:
                    continue
                d = heapq.heappop(maxHeap)[1]
                minHeap.remove((d,d))
            else:
                if len(minHeap) == 0:
                    continue
                d = heapq.heappop(minHeap)[1]
                maxHeap.remove((-d,d))
    if len(maxHeap) == 0:
        return [0,0]
    else:
        maxVal = heapq.heappop(maxHeap)[1]
        minVal = heapq.heappop(minHeap)[1]
        return [maxVal,minVal]
    return answer
# print(solution(["I 16","D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
print(solution((["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))