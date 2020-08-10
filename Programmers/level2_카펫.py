def solution(brown, yellow):
    answer = []
    height = 1
    width = yellow
    while (width >= height):
        if height * 2 + width * 2 + 4 == brown:
            answer = [width + 2, height + 2]
            break
        else:
            while (True):
                height += 1
                if yellow // height == yellow / height:
                    width = yellow // height
                    break
                else:
                    continue

    return answer
print(solution(10,2))
print(solution(24,24))