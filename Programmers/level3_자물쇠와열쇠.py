def rotate(arr):
    n = len(arr)
    rotate_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_arr[n - 1 - j][i] = arr[i][j]
    return rotate_arr
def resetLock(expand_lock,lock,lock_len,key_len):
    for x in range(lock_len):
        for y in range(lock_len):
            expand_lock[key_len - 1 + x][key_len - 1 + y] = lock[x][y]
    return expand_lock
def setKey(expand_lock,key,key_len,i,j):
    for k in range(key_len):
        for l in range(key_len):
            expand_lock[i + k][j + l] += key[k][l]
    return expand_lock
def checkLock(expand_lock,lock_len,key_len):
    for i in range(lock_len):
        for j in range(lock_len):
            if expand_lock[key_len - 1 + i][key_len - 1 + j] == 1:
                continue
            else:
                return False
    return True
def solution(key, lock):
    lock_len = len(lock)
    key_len = len(key)
    expand_len = lock_len + (key_len - 1) * 2
    expand_lock = [[0 for _ in range(expand_len)] for _ in range(expand_len)]
    for _ in range(4):
        key = rotate(key)
        #i,j key 위치 이동
        for i in range(lock_len+key_len-1):
            for j in range(lock_len+key_len-1):
                expand_lock = resetLock(expand_lock,lock,lock_len,key_len)
                expand_lock = setKey(expand_lock,key,key_len,i,j)
                if checkLock(expand_lock,lock_len,key_len):
                    return True
    return False

