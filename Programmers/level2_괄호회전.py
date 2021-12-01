def solution(s):
    answer = 0
    for i in range(0,len(s)):
        i = i % len(s)
        answer += count_valid(s[i:]+s[:i])
    return answer

def count_valid(s):
    cnt = 0
    left = ['(','{','[']
    right = [')','}',']']
    stack = list()
    flag = False
    for c in s:
        if c in left:
            stack.append(c)
        else:
            if stack and (left.index(stack[-1]) == right.index(c)):
                stack.pop()
                flag = True
            else:
                return 0
    if stack:
        return 0
    return 1

print(solution("[](){}")) #3