T=int(input())
for k in range(T):
    K,N,M=map(int,input().split())
    a=list(map(int, input().split()))
    M_list=[0]*(N+1)
    for i in range(len(a)):
        M_list[a[i]]+=1
    count=0
    start=0
    end=K
    
    while True:
        zero=0 #               
        for j in range(start+1, end+1):
            if M_list[j]==1: #충전기가 있다
                start=j 
            else:
                zero+=1
        if zero==K:
            count=0
            break
        
        count+=1
        end=start+K
        
        
        if end>=N:
            break
        
    print("#%d %d"%(k+1,count))
