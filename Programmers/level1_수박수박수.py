def solution(n):
    pattern = "수박"
    return pattern*(n//2)+pattern[:n%2]
