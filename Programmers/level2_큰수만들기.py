'''<그리디> 어려워어려워 시간초과
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수
중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

~~도와주세요~~ test1-5,9,11 통과 test6-8,10 런타임에러 test11 통과 test12 실패'''

def recursion(numberStr,jari): #numberStr의 숫자를 jari의 자릿수로 만들
    leng = len(numberStr)
    if(leng==jari): #만들려는 자릿수랑 지금 수의 자릿수 같으면 얼른 리턴 시켜줌
        return numberStr
    if (leng==1):
        #print(#umberStr)
        return numberStr[0]
    m = max(numberStr[:leng-jari+1])
    index = numberStr.index(m)
    if(index==leng-1):
        #print(0)
        return numberStr[index]
    #print(2)
    return str(m) + recursion(numberStr[index+1:],jari-1)
def solution(number, k):
    length = len(number)
    p = length-k
    return recursion(number,p)
print(solution("1231234",3))
