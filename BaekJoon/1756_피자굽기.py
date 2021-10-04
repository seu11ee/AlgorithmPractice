d,n = map(int,input().split())
oven = list(map(int,input().split()))
pizzas = list(map(int,input().split()))

idx = d - 1

for i in range(1,len(oven)):
    oven[i] = min(oven[i-1],oven[i])

def binary_search(left, right, oven_list, pizza_value):
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        #안걸림
        if oven_list[mid] >= pizza_value:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


for pizza in pizzas:
    idx = binary_search(0, idx, oven, pizza)
    # 갈데가 업슴
    if idx == -1:
        idx -= 1
        break
    # 들어갈 곳 찾음
    else:
        idx -= 1

print(idx+2)
