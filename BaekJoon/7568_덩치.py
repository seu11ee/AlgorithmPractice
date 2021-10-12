from itertools import combinations
import sys

n = int(sys.stdin.readline())
infos = []
records = [1 for _ in range(n)]

for _ in range(n):
    height, weight = map(int,sys.stdin.readline().split())
    infos.append([height,weight])

for a, b in combinations(range(n),2):
    a_info = infos[a]
    b_info = infos[b]
    if a_info[0] > b_info[0] and a_info[1] > b_info[1]:
        records[b] += 1
    elif a_info[0] < b_info[0] and a_info[1] < b_info[1]:
        records[a] += 1

print(*records)
