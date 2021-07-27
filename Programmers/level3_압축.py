def solution(msg):
    dictionary = dict()
    last = 26
    answer = []
    ordKey = 65
    for i in range(last):
        dictionary[chr(ordKey+i)] = i+1
    length = len(msg)
    i = 0
    while i < length:
        j = i+1
        while j < length+1:
            if msg[i:j] not in dictionary.keys():
                break
            j+=1
        j-=1
        w = msg[i:j]
        k = dictionary[w]
        answer.append(k)
        if j < length:
            c = msg[j]
        else:
            break
        wc = w+c
        if wc not in dictionary.keys():
            last,dictionary = addToDictionary(wc,last,dictionary)
        i = j
    return answer
def addToDictionary(word,last,dictionary):
    last += 1
    dictionary[word] = last
    return last,dictionary

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))