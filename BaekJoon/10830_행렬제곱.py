n,b = map(int,input().split())
a = []
p = 1000
for _ in range(n):
    a.append(list(map(int,input().split())))
def productMatrix(X,Y):
    answer = [[(sum((a%p)*(b%p) for a, b in zip(X_row, Y_col)))%p for Y_col in zip(*Y)] for X_row in X]
    return answer
def powerMatrix(mat,e):
    if e == 1:
        new = []
        for i in mat:
            temp = []
            for j in i:
                temp.append(j%1000)
            new.append(temp)
        return new
    temp = powerMatrix(mat,e//2)
    if e % 2 == 0:
        return productMatrix(temp,temp)
    else:
        return productMatrix(productMatrix(temp,temp),a)
answer = powerMatrix(a,b)

for i in answer:
    for j in i:
        print(j,end = " ")
    print()

