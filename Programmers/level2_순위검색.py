from collections import defaultdict

def solution(info, query):
    answer = []
    infos = defaultdict(set)
    scores = list()
    for i in range(len(info)):
        for j in info[i].split(" "):
            if j.isnumeric():
                scores.append(j)
            infos[j].add(i)
    for i in query:
        result_set = set(range(len(info)))
        temp_query = i.split(" and ")
        temp_query.append("")
        temp_query[-2:] = temp_query[-2].split(" ")
        for j in temp_query:
            if j == "-":
                continue
            elif j.isdecimal():
                result_set = set(filter(lambda x:int(scores[x])>=int(j),result_set))
            else:
                result_set = result_set.intersection(infos[j])
        answer.append(len(result_set))
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))