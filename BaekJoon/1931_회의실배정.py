import sys

n = int(sys.stdin.readline())
meeting_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
end = -1
meeting_list.sort(key=lambda x: (x[1],x[0]))
count = 0
for meeting in meeting_list:
    if meeting[0] >= end:
        end = meeting[1]
        count += 1

print(count)