from collections import defaultdict


def solution(genres, plays):
    cnt_dict = defaultdict(int)
    idx_dict = defaultdict(list)
    answer = []
    n = len(genres)

    for i in range(n):
        cnt_dict[genres[i]] += plays[i]
        idx_dict[genres[i]].append((plays[i], i))
    cnt_dict = dict(sorted(cnt_dict.items(), key=lambda x: -x[1]))

    for key in cnt_dict.keys():
        idx_dict[key].sort(key=lambda x: (-x[0], x[1]))
        if len(idx_dict[key]) > 2:
            idx_dict[key] = idx_dict[key][:2]
        for play, idx in idx_dict[key]:
            answer.append(idx)
    return answer