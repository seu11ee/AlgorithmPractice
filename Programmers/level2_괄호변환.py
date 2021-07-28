def solution(p):
    answer = ''
    answer = checkEven(p)

    return answer


def checkEven(w):
    length = len(w)
    if length == 0:
        return ''
    i = 0
    left = 0
    right = 0
    while (i < length):
        if w[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            u = w[:i + 1]
            v = w[i + 1:]
            break
        i += 1
    if checkRight(u):
        return u + checkEven(v)
    else:
        return "(" + checkEven(v) + ")" + u[-2:0:-1]


def checkRight(u):
    stack = []
    for i in u:
        if not stack:
            stack.append(i)
        else:
            top = stack[-1]
            if top == "(" and i == ")":
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        return True
    return False


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))