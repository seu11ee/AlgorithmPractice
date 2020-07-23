import sys
from collections import deque
def solution(name_list):
    length = len(name_list)
    answer = False
    for i in range(name_list):
        for j in range(i+1,length):
            if set(name_list[i]) and set(name_list[j]):
                answer = True
                break

