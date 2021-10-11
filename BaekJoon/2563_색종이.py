n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
answer = 0
for i in range(n):
    x,y = map(int,input().split())
    for j in range(10):
        for k in range(10):
            if paper[y-1+j][x-1+k] == 0:
                answer += 1
                paper[y-1+j][x-1+k] = 1
print(answer)