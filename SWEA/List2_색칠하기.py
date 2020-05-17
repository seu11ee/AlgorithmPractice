'''r1,c1)부터 (r2,c2)까지 색칠하고 컬러 겹치는 부분의 면적 찾는 문제
순서쌍은 튜플로 나타내고 컬러에 따라 다른 set에 넣어준다.
사각형의 양 끝점이 주어질때 중첩 for문으로 모든 순서쌍 구한다.
set들의 교집합을 intersection 함수로 구하고 len해준다. (세화가 알려줌 ㅎㅌㅎㅌ)'''

T = int(input())
for i in range(T):
    N = int(input())
    red_set = set()
    blue_set = set()
    for j in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                if color == 1:
                    red_set.add((x,y))
                else :
                    blue_set.add((x,y))

    print("#%d %d"%(i+1,len(red_set.intersection(blue_set))))


        
