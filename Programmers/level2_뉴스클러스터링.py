from collections import defaultdict

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set_str1 = set()
    set_str2 = set()
    dict_str1 = defaultdict(int)
    dict_str2 = defaultdict(int)
    #str1,str2의 다중집합 만들기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            set_str1.add(str1[i:i+2])
            dict_str1[str1[i:i+2]] += 1
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            set_str2.add(str2[i:i+2])
            dict_str2[str2[i:i+2]] += 1
    #str1,str2 교집합 합집합 구하기
    intersection = set_str1.intersection(set_str2)
    union = set_str1.union(set_str2)
    inter_cnt = 0
    union_cnt = 0
    #str1,str2 다중집합 교집합수, 합집합 수 구하기
    for i in intersection:
        inter_cnt += min(dict_str1[i],dict_str2[i])
    for u in union:
        union_cnt += max(dict_str1[u],dict_str2[u])
    if len(set_str1) == 0 and len(set_str2) == 0:
        answer = 1
    else:
        answer = inter_cnt/union_cnt
    answer = int((answer)*65536)
    return answer

print(solution("FRANCE","french"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))