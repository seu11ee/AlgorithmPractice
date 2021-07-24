from sys import stdin
from collections import deque

input_string = stdin.readline()
stack = deque()

try:
    for s in input_string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            p = stack.pop()
            number_list = []
            while(True):
                if p == '(':
                    if len(number_list) == 0:
                        stack.append(2)
                    else:
                        stack.append((sum(number_list)) * 2)
                    break
                else:
                    number_list.append(p)
                    p = stack.pop()
        elif s == ']':
            p = stack.pop()
            number_list = []
            while (True):
                if p == '[':
                    if len(number_list) == 0:
                        stack.append(3)
                    else:
                        stack.append((sum(number_list)) * 3)
                    break
                else:
                    number_list.append(p)
                    p = stack.pop()
    print(sum(stack))
except:
    print(0)


# for s in input_string:
#     if s == '(' or s == '[':
#         queue.append(s)
#     elif s == ')':
#         p = queue.pop()
#         number_list = []
#         while(True):
#             if p == '(':
#                 if len(number_list) == 0:
#                     queue.append(2)
#                 else:
#                     queue.append((sum(number_list))*2)
#                 break
#             else:
#                 number_list.append(p)
#                 p = queue.pop()
#     elif s == ']':
#         p = queue.pop()
#         number_list = []
#         while (True):
#             if p == '[':
#                 if len(number_list)==0:
#                     queue.append(3)
#                 else:
#                     queue.append((sum(number_list)) * 3)
#                 break
#             else:
#                 number_list.append(p)
#                 p = queue.pop()
# print(sum(queue))





