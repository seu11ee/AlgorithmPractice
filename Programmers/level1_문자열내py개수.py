'''문자열 count 함수 이용가능'''
def solution(s):
    pCount = 0
    yCount = 0
    for char in s:
        if (char == 'p' or char == 'P'):
            pCount += 1
        elif (char == 'y' or char == 'Y'):
            yCount += 1
    if pCount == yCount:
        if pCount == 0:
            return False
        else:
            return True
    else:
        return False
    
print(solution("pPoooyY"))
print(solution("Pyy"))

def solution2(s):
    s.lower()
    pCount = s.count('p')
    yCount = s.count('y')
    if pCount==yCount:
        if pCount == 0:
            return False
        else:
            return True
    else:
        return False
