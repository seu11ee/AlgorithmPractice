'''N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.

1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.

주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.'''
from collections import deque
T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    oven_queue = deque()
    pizza_list = list(map(int,input().split()))
    m=0
    for n in range(N): #화덕을 피자로 채움
        oven_queue.append([pizza_list[n],n+1])
        #print(oven_queue)
    m = N

    while(True):
        oven_queue[0][0]=oven_queue[0][0]//2
        #print("1",oven_queue)
        if oven_queue[0][0]==0: #치즈가 다 녹았을때
            oven_queue.popleft()
            #print("2",oven_queue)
            if m<M:
                oven_queue.appendleft([pizza_list[m],m+1])
                m+=1
                oven_queue.rotate(-1)
            else:
                if len(oven_queue)==1:
                    answer = oven_queue.pop()
                    break
        else:
            oven_queue.rotate(-1)

    print("#%d %d"%(t,answer[1]))











