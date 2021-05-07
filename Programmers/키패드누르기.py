def solution(numbers, hand):
    answer = ''
    leftNumber = (1,4,7)
    rightNumber = (3,6,9)
    leftHand = [3,0]
    rightHand = [3,2]
    numberToPoint = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

    for number in numbers:
        if number in leftNumber:
            answer += "L"
            leftHand = numberToPoint[number]
        elif number in rightNumber:
            answer += "R"
            rightHand = numberToPoint[number]
        else:
            numberPoint = numberToPoint[number]
            leftDist = abs(leftHand[0]-numberPoint[0])+abs(leftHand[1]-numberPoint[1])
            rightDist = abs(rightHand[0]-numberPoint[0])+abs(rightHand[1]-numberPoint[1])
            if leftDist > rightDist:
                answer += "R"
                rightHand = numberToPoint[number]
            elif leftDist < rightDist:
                answer += "L"
                leftHand = numberToPoint[number]
            else:
                if hand == "left":
                    answer += "L"
                    leftHand = numberToPoint[number]
                else:
                    answer += "R"
                    rightHand = numberToPoint[number]

    return answer