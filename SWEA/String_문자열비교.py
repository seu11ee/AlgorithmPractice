T = int(input())
for t in range(T):
    a = input()
    b = input()
    print("#%d"%(t+1),end=" ")
    if b.count(a):
        print(1)
    else:
        print(0)