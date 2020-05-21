'''수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을
 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
input 5 17 output 4'''
#숨바꼭질
#BFS
#BFS는 큐이용!

from sys import stdin
from collections import deque #시간절  list.pop(0) 은 시간복잡도가 O(N) 이라 이렇게 구현하면 시간적으로 매우 비효율적인 코드가 만들어지게 됩니다.

N,K = map(int,stdin.readline().split())
i = 0
queue = deque()
queue.append((i,N))
while(queue):

    now = queue.popleft()
    i = now[0]
    if (now[1]==K):
        print(i)
        break
    newN = now[1]
    if(0<=newN*2<=100000):
        queue.append((i + 1, newN * 2))
    if(0<=newN+1<=100000):
        queue.append((i + 1, newN + 1))
    if(0<=newN-1<=100000):
        queue.append((i+1,newN-1))


'''
1차시도:메모리초과
from sys import stdin
from collections import deque #시간절  list.pop(0) 은 시간복잡도가 O(N) 이라 이렇게 구현하면 시간적으로 매우 비효율적인 코드가 만들어지게 됩니다.

N,K = map(int,stdin.readline().split())
i = 0
queue = deque()
queue.append((i,N))
while(queue):
    now = queue.popleft()

    i = now[0]
    if (now[1]==K):
        print(i)
        break
    newN = now[1]

    queue.append((i+1,newN-1))
    queue.append((i+1,newN+1))
    queue.append((i+1,newN*2))'''








