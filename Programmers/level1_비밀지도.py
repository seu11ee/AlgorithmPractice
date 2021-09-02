def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in arr1:
        map1.append(decimal_to_binary(i, n))
    for i in arr2:
        map2.append(decimal_to_binary(i, n))
    for i in range(n):
        temp = ""
        for j in range(n):
            #0은 공백 1은 벽
            if bool(map1[i][j]) or bool(map2[i][j]):
                temp += "#"
            else:
                temp += " "
        answer.append(temp)

    return answer


def decimal_to_binary(decimal_num, size):
    binary_list = []
    dividers = []
    for i in range(size - 1, -1, -1):
        dividers.append(2 ** i)
    for i in dividers:
        if decimal_num // i > 0:
            binary_list.append(1)
            decimal_num = decimal_num % i
        else:
            binary_list.append(0)
    return binary_list

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
#["#####", "# # #", "### #", "#  ##", "#####"]