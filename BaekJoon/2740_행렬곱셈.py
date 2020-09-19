n,m = map(int,input().split())
mat1 = []
mat2 = []
for _ in range(n):
    mat1.append(list(map(int,input().split())))
m,k = map(int,input().split())
for _ in range(m):
    mat2.append(list(map(int,input().split())))
def productMatrix(X,Y):
    answer = [[sum((a * b) for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return answer
answer = productMatrix(mat1,mat2)
for i in answer:
    for j in i:
        print(j,end=" ")
    print()
