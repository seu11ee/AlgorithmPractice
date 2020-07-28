import sys

N,M = map(int,sys.stdin.readline().split())

lesson = list(map(int,sys.stdin.readline().split()))
binary = list()
sum_list = list()
left = 0
right = len(lesson)-1
mid = (left+right)//2
temp = lesson
while(len(binary)!=M):
    binary.pop()
    a = temp[left:mid+1]
    b = temp[mid+1:right+1]
    binary.append((left,mid))
    sum_list = sum(a)
    binary.append((mid+1,right))
    sum_list = sum(b)
    next = binary[sum_list.index(min(sum_list))]
    left = next[0]
    right = next[1]
    mid = (left+right)//2




