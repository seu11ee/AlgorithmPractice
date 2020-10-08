import sys

mushroom = [int(sys.stdin.readline()) for _ in range(10)]
sum = [0 for _ in range(10)]
sum[0] = mushroom[0]
if sum[0]>=100:
    print(sum[0])
else:
    for i in range(1,10):
        sum[i] = sum[i-1]+mushroom[i]
        if sum[i-1]<=100 and sum[i]>=100:
            break
    a = 100-sum[i-1]
    b = sum[i]-100
    if a<b:
        print(sum[i-1])
    else:
        print(sum[i])



