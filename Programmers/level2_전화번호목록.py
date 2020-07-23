def solution(phone_book):
    answer = True
    length = len(phone_book)
    for i in range(length):
        for j in range(i+1,length):
            iLen = len(phone_book[i])
            jLen = len(phone_book[j])
            if iLen<jLen:
                if phone_book[i] == phone_book[j][:iLen]:
                    answer = False
                    return answer
            else:
                if phone_book[j] == phone_book[i][:jLen]:
                    answer = False
                    return answer
    return answer
