def solution(triangle):
    n = len(triangle)
    for i in range(n-1,0,-1):
        for j in range(i):
            a = triangle[i-1][j]
            b = triangle[i][j]
            c = triangle[i][j+1]
            triangle[i-1][j] = max(a+b,a+c)

    return triangle[0][0]