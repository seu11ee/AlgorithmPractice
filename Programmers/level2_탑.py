'''<스택>탑이 왼쪽으로 신호를 쏠 때 수신가능한 탑은 송신한 탑보다 키가 큰 애들'''
def solution(heights):
    num = len(heights)
    answer =[0]*num
    for i in range(num-1,0,-1): #역순으로 간다는걸 기억하기
        for j in range(i-1,-1,-1):
            if heights[i]<heights[j]:
                answer[i]= j+1
                break
    return answer
print(solution([3,9,9,3,5,7,2]))
