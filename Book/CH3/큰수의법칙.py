from sys import stdin
n,m,k = map(int,stdin.readline().split())
input_list = list(map(int,stdin.readline().split()))
input_list.sort(reverse=True)
answer = 0
mCnt = 0
i = 0
kCnt = 0
while(mCnt < m):
    mCnt += 1
    if kCnt == k:
        i += 1
        kCnt = 0
        if input_list[i]<input_list[i-1]:
            answer += input_list[i]
        i = 0
    else:
        answer += input_list[i]
        kCnt += 1
print(answer)

# 수학적으로 접근해서 풀기

first = input_list[0]
second = input_list[1]

firstCnt = m//(k+1)*k + m%(k+1)
secondCnt = m//(k+1)

print(first*firstCnt + second*secondCnt)


