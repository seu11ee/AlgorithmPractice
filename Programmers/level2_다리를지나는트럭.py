from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque()
    q.append(truck_weights[0])
    sec = 0
    i = 1
    truckCnt = len(truck_weights)
    s = truck_weights[0]
    while s>0:

        sec += 1
        length = len(q)
        if i>=truckCnt:
            if length < bridge_length:
                q.append(0)
            else:
                q.popleft()
                q.append(0)
        else:

            if length == 0:
                q.append(truck_weights[i])
                i += 1
            elif length == bridge_length:
                first = q.popleft()
                s -= first
                if s+truck_weights[i]<= weight:
                    q.append(truck_weights[i])
                    i += 1
                else:
                    q.append(0)
            else:
                if (s+truck_weights[i]) <= weight:
                    if length + 1 <= bridge_length:
                        q.append(truck_weights[i])
                        i += 1
                else:
                    q.append(0)
        s = sum(q)

    return sec+1
print(solution(100,100,[10]))
