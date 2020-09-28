import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
operator = list(map(int,sys.stdin.readline().split()))
answer = []
temp = number[0]
def calculate(num,idx):
    global temp
    if idx == 0:
        temp += num
        return
    if idx == 1:
        temp -= num
        return
    if idx == 2:
        temp *= num
        return
    if idx == 3:
        if temp < 0 :
            temp = -((-temp)//num)
            return
        else:
            temp = temp // num
            return

def recursive(times):
    global temp
    if times == n:
        answer.append(temp)

        return
    for idx,val in enumerate(operator):
        if val != 0:
            operator[idx] -= 1
            origin = temp
            calculate(number[times],idx)
            recursive(times+1)
            temp = origin
            operator[idx] += 1
recursive(1)
print(max(answer))
print(min(answer))


