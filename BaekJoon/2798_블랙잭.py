import sys
N,M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
def choose_card(idx,sub_sum,cnt):
    global M, cards
    values = []
    if cnt == 3 and idx < N+1:
        return sub_sum
    elif idx == N and cnt < 3:
        return 0
    for i in range(2):
        if sub_sum + cards[idx]*i <= M:
            values.append(choose_card(idx+1,sub_sum + cards[idx]*i,cnt))
        cnt += 1
    return max(values)
print(choose_card(0,0,0))
