from itertools import permutations

def solution(expression):
    answer = []
    temp = ""
    operators = ("*","-","+")
    operator_list = list(permutations(operators,3))
    expression_list = []
    postfix = [[] for _ in range(6)]
    for i in expression:
        if i in operators:
            expression_list.append(temp)
            expression_list.append(i)
            temp = ""
        else:
            temp += i
    expression_list.append(temp)
    #연산자 우선순위에 따라 후위수식으로 변경
    for i in range(len(operator_list)):
        stack = []
        for j in expression_list:
            #입력이 연산자인 경우
            if j in operators:
                if stack:
                    if operator_list[i].index(stack[-1]) <= operator_list[i].index(j):
                        while stack:
                            if operator_list[i].index(stack[-1]) > operator_list[i].index(j):
                                break
                            else:
                                postfix[i].append(stack.pop())
                    stack.append(j)
                else:
                    stack.append(j)
            #입력이 피연산자인 경우
            else:
                postfix[i].append(j)
        #stack에 남은 수식들을 postfix[i]에 입력
        while stack:
            postfix[i].append(stack.pop())
        #후위수식을 계산
        stack = []
        for j in postfix[i]:
            if j not in operators:
                stack.append(j)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if j == "*":
                    stack.append(a*b)
                elif j == "-":
                    stack.append(a-b)
                elif j == "+":
                    stack.append(a+b)
        answer.append(abs(stack.pop()))
    return max(answer)

print(solution("100-200*300-500+20"))