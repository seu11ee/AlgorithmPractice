import sys


t = int(sys.stdin.readline())
dp1 = ["","7","1"]
dp2 = ["","10","1","7","4","2","6","8","10","18","22"]

def dp_max(x):
    a = x // 2
    b = x % 2
    if b == 1:
        a -= 1
    return dp1[b] + dp1[2] * a


def dp_min(x):
    if x < 11:
        return dp2[x]
    ret = "8"*((x + 6) // 7)
    if x % 7 == 1: ret="10"+ret[2:]
    elif x % 7 == 2: ret="1"+ret[1:]
    elif x % 7 == 3:
        ret = "200" + ret[3:]
    elif x % 7 == 4: ret="20"+ret[2:]
    elif x % 7 == 5: ret="2"+ret[1:]
    elif x % 7 == 6: ret="6"+ret[1:]
    return ret


for _ in range(t):
    n = int(sys.stdin.readline())

    print(dp_min(n), dp_max(n))
