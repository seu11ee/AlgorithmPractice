'''<그리디> 어려워어려워 시간초과
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수
중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

~~도와주세요~~ test1-5 통과 test6-10 런타임에러 test11 통과 test12 실패'''

def recursion(l,num):
    leng = len(l)
    if (leng==1):
        return str(l[0])
    m = max(l[:leng-num+1])
    index = l.index(m)
    if(index==leng-1):
        return l[index]
    return str(m) + recursion(l[l.index(m)+1:],num-1)
def solution(number, k):
    length = len(number)
    p = length-k
    return recursion(number,p)
print(solution("1924",2))