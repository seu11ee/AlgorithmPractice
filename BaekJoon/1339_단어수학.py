from collections import defaultdict
n = int(input())
coefficient = defaultdict(int)

for _ in range(n):
    word = input()
    word_length = len(word)
    for i in range(word_length):
        coefficient[word[i]] += 10 ** (word_length - i - 1)
answer = 0
dict_values = list(coefficient.values())
dict_values.sort(reverse=True)
numbers = list(range(10))
for value in dict_values:
    answer += value*numbers.pop()

print(answer)



