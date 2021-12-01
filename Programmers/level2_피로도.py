from itertools import permutations


def solution(k, dungeons):
    answers = []
    for ordered_dungeons in permutations(dungeons):
        answers.append(calculate(k, ordered_dungeons))

    return max(answers)


def calculate(k, dungeons):
    cnt = 0
    for dungeon in dungeons:
        minimum, spend = dungeon
        if k < minimum:
            break
        k -= spend
        cnt += 1

    return cnt