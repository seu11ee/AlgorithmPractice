#124나라에는 0이 없기 때문에 n -> n-1로 해서 계산한다.
def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]



