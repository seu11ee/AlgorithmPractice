def is_palindrome(s):
    if s == s[::-1]:
        return True
def solution(s):
    max_length = 0
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if is_palindrome(s[i:j]):
                length = j-i
                if length > max_length:
                    max_length = length
                break
    return max_length