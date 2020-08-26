from collections import Counter

def solution(participant, completion):
    all = Counter(participant)
    comple = Counter(completion)
    answerSet = all - comple
    answer = list(answerSet).pop()
    return answer