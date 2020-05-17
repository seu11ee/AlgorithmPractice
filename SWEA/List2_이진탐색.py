'''이진탐색으로 책 페이지수 빨리 찾'''
T = int(input())
for t in range(1,T+1):
    P,Pa,Pb = map(int,input().split())
    La,Ra,Lb,Rb = 1,P,1,P
    Ca = (La + Ra) // 2
    Cb = (Lb + Rb) // 2
    while(True):
        if(Ca==Pa and Cb==Pb):
            winner = 0
            break
        if (Ca==Pa):
            winner = 'A'
            break
        elif (Ca < Pa):
            La = Ca
        elif (Ca > Pa):
            Ra = Ca
        if (Cb==Pb):
            winner = 'B'
            break
        elif (Cb < Pb):
            Lb = Cb
        elif (Cb > Pb):
            Rb = Cb
        Ca = (La + Ra) // 2
        Cb = (Lb + Rb) // 2
    print("#%d"%t,winner)








