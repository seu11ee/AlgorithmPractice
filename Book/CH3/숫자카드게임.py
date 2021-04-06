from sys import stdin

n, m = map(int, stdin.readline().split())
input_list = []
for i in range(n):
    input_list.append(min(map(int, stdin.readline().split())))
print(max(input_list))