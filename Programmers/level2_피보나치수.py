'''
프로그래머스 풀이
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
'''

def fibo(num):
    arr = [0,1]
    if num == 0 or num == 1:
        return arr[num]
    else:
        i = 2
        while(i<=num):
            arr.append(arr[i-2]+arr[i-1])
            i += 1
        return arr[num]
def solution(n):
    answer = fibo(n)%1234567
    return answer