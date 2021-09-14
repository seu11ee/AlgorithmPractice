import sys
from itertools import permutations
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
max_sum = 0
for numbers in permutations(A):
    sub_sum = 0
    for i in range(n-1):
        sub_sum += abs(numbers[i]-numbers[i+1])
    if sub_sum > max_sum:
        max_sum = sub_sum

print(max_sum)