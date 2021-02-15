from sys import stdin

n = int(stdin.readline())

student = []

for _ in range(n):
    inputValue =  list(stdin.readline().split())
    inputValue = inputValue[0:1] + list(map(int,inputValue[1:]))
    student.append(inputValue)


student.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in student:
    print(i[0])
