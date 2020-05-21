from collections import Counter
T = int(input())
for t in range(T):
    str1 = list(input())
    str2 = input()
    counter = Counter(str2)
    str1_dict=dict()
    for char in str1:
        if char in counter.keys():
            str1_dict[char]=counter.get(char)
    print("#%d %d"%(t+1,max(str1_dict.values())))


