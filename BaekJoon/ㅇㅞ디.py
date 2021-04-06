answer = []
for i in range(450):
    if (i-5)%6 == 0 and (i-4)%5 == 0 and (i-3)%4 == 0:
        print(i)
        answer.append(i)
print(answer)