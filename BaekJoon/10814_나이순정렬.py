import sys
n = int(sys.stdin.readline())
class Member:
    def __init__(self,age,name):
        self.age = age
        self.name = name
memberList=[]
for _ in range(n):
    input_age,input_name = sys.stdin.readline().split()
    memberList.append(Member(int(input_age),input_name))
memberList.sort(key = lambda member:member.age) #람다식 : member를 받아서 member.age 반환
for item in memberList:
    print("%d %s"%(item.age,item.name))

