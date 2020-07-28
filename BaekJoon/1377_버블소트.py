import sys
def bubble1():
    N = int(sys.stdin.readline())
    A = [-1]
    for n in range(1,N+1):
        A.append(int(sys.stdin.readline()))
    change = False
    for i in range(1,N+2):
        change = False
        for j in range(1,N-i+1):
            if A[j]>A[j+1]:
                change = True
                A[j],A[j+1] = A[j+1],A[j]
        if not change:
            print(i)
            break
def bubble2():
    N = int(sys.stdin.readline())
    A = [-1]
    for n in range(1, N + 1):
        A.append(int(sys.stdin.readline()))
    i = 1

    while(True):
        maxValue = max(A)
        if maxValue==A[-1]:
            print(i)
            break
        else:
            A.remove(maxValue)
            i+=1
def bubble3():
    N = int(sys.stdin.readline())
    A = [-1]
    for n in range(1,N+1):
        A.append(int(sys.stdin.readline()))
    c=1
    for i in range(1,N):
        if A[i]>A[i+1]:
            c+=1
    print(c)
def bubble4():
    N = int(sys.stdin.readline())
    A = [(-1,0)]
    result = [-1]
    for n in range(1, N + 1):
        A.append((int(sys.stdin.readline()),n))
    #print(A)
    A.sort()
    for a in range(1,N+1):
        result.append(A[a][1]-a)
    print(max(result)+1)
bubble4()



