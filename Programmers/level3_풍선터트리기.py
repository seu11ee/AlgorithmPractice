INF = int(1e9)


def solution(a):
    answer = 0
    min_left = a[:]
    min_right = a[:]
    for i in range(1, len(a)):
        if a[i] < min_left[i - 1]:
            min_left[i] = a[i]
        else:
            min_left[i] = min_left[i - 1]
    for i in range(len(a) - 2, -1, -1):
        if a[i] < min_right[i + 1]:
            min_right[i] = a[i]
        else:
            min_right[i] = min_right[i + 1]
    for i in range(len(a)):
        left = min_left[i - 1] if i > 0 else INF
        right = min_right[i + 1] if i < len(a) - 1 else INF
        is_left_greater = left > a[i]
        is_right_greater = right > a[i]
        if is_left_greater or is_right_greater:
            answer += 1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))  # 6
