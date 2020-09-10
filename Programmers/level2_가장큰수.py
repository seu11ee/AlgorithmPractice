def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: (x*3), reverse = True)
    return int(str("".join(numbers)))


print(solution([6,2,10]))