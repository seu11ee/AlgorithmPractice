def recursion(numberStr,jari): #numberStr의 숫자를 jari의 자릿수로 만들
    leng = len(numberStr)
    if(leng==jari): #만들려는 자릿수랑 지금 수의 자릿수 같으면 얼른 리턴 시켜줌
        return numberStr
    if (jari==1):
        #print(#umberStr)
        return max(numberStr)
    m = max(numberStr[:leng-jari+1])
    index = numberStr.index(m)
    #print(2)
    return str(m) + recursion(numberStr[index+1:],jari-1)
def solution(number, k):
    length = len(number)
    p = length-k
    return recursion(number,p)

print(solution("1231234",3))