from collections import deque
def solution(begin, target, words):
    answer = []
    stack = deque()
    stack.append(begin)
    visit = set()
    visit.add(begin)
    temp_answer = 0
    if target not in words:
        return 0
    while stack:
        begin = stack.pop()
        if begin == target:
            answer.append(temp_answer)
            temp_answer = 0
        temp_answer += 1
        for word in words:
            if word not in visit and findTarget(begin,word):
                stack.append(word)
                visit.add(word)
    if answer:
        return min(answer)
    return 0
def findTarget(str1, str2):
    length = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            length += 1
    if length + 1 == len(str1):
        return True
    return False