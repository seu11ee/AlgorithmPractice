from sys import stdin
from itertools import combinations
inputList = list(map(int,stdin.readline().split()))
while inputList[0] != 0:
    n = inputList[0]
    a = inputList[1:]
    for i in combinations(a,6):
        for j in i:
            print(j,end = " ")
        print()
    print()
    inputList = list(map(int, stdin.readline().split()))