from collections import deque
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    q = deque(enumerate(prices))
    observe = []

    while (q):

        idx, val = q.popleft()
        #내가 관찰하고자 하는 것들의 인덱스
        temp = observe[:]
        for i in temp:
            answer[i] += 1

            #주식 가격이 떨어지면 observe 리스트에서 인덱스값 삭제
            if prices[i] > val:
                observe.remove(i)
        observe.append(idx)

    return answer

print(solution([1,2,3,2,3,3,1]))