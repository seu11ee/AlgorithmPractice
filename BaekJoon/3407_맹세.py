# import sys
# from collections import deque
# element = {
# 	'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u',"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
# 	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
# 	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
# 	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
# 	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
# 	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
# 	"pu", "ru", "lv", "dy"
# 	}
#
# n = int(sys.stdin.readline())
# input_list = [sys.stdin.readline() for _ in range(n)]
# visit = set()
# for word in input_list:
#     answer = "NO"
#     queue = deque()
#     queue.append(0)
#     visit.add(0)
#     while(queue):
#         idx = queue.popleft()
#         print(queue)
#         if idx == len(word)-1:
#             if word[idx] in element:
#                 answer = "YES"
#                 break
#         if idx == len(word)-2:
#             if word[idx:idx+2] in element:
#                 answer = "YES"
#                 break
#         if word[idx] in element and idx+1 not in visit:
#             visit.add(idx+1)
#             queue.append(idx+1)
#         if word[idx:idx+2] in element and idx+2 not in visit:
#             visit.add(idx+2)
#             queue.append(idx+2)
#
#     print(answer)

import sys
from collections import deque
element = {
	'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u',"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"
	}

n = int(sys.stdin.readline())
input_list = [sys.stdin.readline() for _ in range(n)]
visit = set()
for word in input_list:
    answer = "NO"
    queue = deque()
    queue.append((0,0))
    while(queue):
        start,end = queue.popleft()

        if (start,end) not in visit:
            print(word[start:end + 1])
            visit.add((start,end))
            if end == len(word)-1:
                if word[start:end+1] in element:
                    answer = "YES"
                    break
            if word[start:end+1] in element:
                if start == end:
                    queue.append((start,end+1))
                    queue.append((end+1,end+1))
                else:
                    queue.append((end,end))
                    queue.append((end,end+1))
    print(answer)