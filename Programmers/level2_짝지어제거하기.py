def solution(s):
    p1 = 0
    p2 = 1
    removed = [False for _ in range(len(s))]
    stack = list()
    while p2 < len(s):
        # 짝찾음
        if s[p1]==s[p2]:
            removed[p1] = True
            removed[p2] = True
            if stack:
                if p1 == stack[-1]:
                    stack.pop()
            if stack:
                p1 = stack.pop()
                p2 += 1
            else:
                p1 = p2 + 1
                p2 = p1 + 1
        else:
            stack.append(p1)
            p1 = p2
            p2 += 1

    if False in removed:
        answer = 0
    else:
        answer = 1
    return answer