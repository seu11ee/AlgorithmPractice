def fibo_matric(A, n):
    if n == 1:
        for i in range(2):
            for j in range(2):
                A[i][j] %= 1000000
        return A
    elif n % 2 == 1:
        tmp = [[0, 0], [0, 0]]
        B = fibo_matric(A, n - 1)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tmp[i][j] += B[i][k] * A[k][j]
                tmp[i][j] %= 1000000
        return tmp
    else:
        tmp = [[0, 0], [0, 0]]
        B = fibo_matric(A, n // 2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tmp[i][j] += B[i][k] * B[k][j]
                tmp[i][j] %= 1000000
        return tmp


n = int(input())
A = [[1, 1], [1, 0]]
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(fibo_matric(A, n - 1)[0][0])



