from itertools import combinations

def solution(relation):
    answer = []
    n = len(relation)
    numberOfColumns = len(relation[0])
    coms = []
    cols = range(numberOfColumns)
    for i in range(1,numberOfColumns+1):
        coms.extend(map(set,combinations(cols,i)))
    #coms는 가능한 column 인덱스 조합 리스트
    for com in coms:
        flag = True
        for ans in answer:
            if ans.issubset(com):
                flag = False
                break
        if flag:
            if checkCandidate(relation,com,n):
                answer.append(com)
    return len(answer)
def checkCandidate(relation,columns,n):
    check_set = set()
    for i in range(n):
        temp = list()
        for column in columns:
            temp.append(relation[i][column])
        if tuple(temp) in check_set:
            return False
        check_set.add(tuple(temp))
    return True

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])) #2