import sys
P = 1000000007
N,K = map(int,sys.stdin.readline().split())
fact = [1 for _ in range(N+1)]

i = 2
while(i<N+1):
    fact[i] = fact[i-1]*i%P
    i+=1
def square(n,e):
    if e%2 == 0:
        #리턴값주의
        return (square(n,e//2)**2)%P
    elif e%2 == 1:
        if e == 1:
            return n
        return (square(n,e//2)**2*n)%P
answer = fact[N]%P*square(fact[K]*fact[N-K],P-2)%P

print(answer)


