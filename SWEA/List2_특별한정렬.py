'''가장큰수->가장작은수->두번째큰수->두번째작은수... 정렬'''
def mySort(myList):
    newList =[]
    for i in range(10):
        if i%2==0:
            temp = max(myList)
        else:
            temp = min(myList)
        newList.append(temp)
        myList.remove(temp)
    return newList

T = int(input())
for t in range(1,T+1):
    N = int(input())
    int_list = list(map(int,input().split()))
    print("#%d"%t,end=" ")
    for i in mySort(int_list):
        print(i,end=" ")
    print()




