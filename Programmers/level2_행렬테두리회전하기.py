def solution(rows, columns, queries):
    answer = []
    square = []
    number = 1
    for x in range(rows):
        square.append(list(range(number, number + columns)))
        number += columns
    for query in queries:
        min_value, square = rotate(square, query)
        answer.append(min_value)
    return answer


def rotate(matrix, query):
    x1, y1, x2, y2 = query
    width = y2 - y1
    height = x2 - x1
    numbers = []

    x = x1 - 1
    y = y1
    flag = 1
    for _ in range(2):
        for _ in range(width):
            numbers.append(matrix[x][y])
            y += 1 * flag
        y -= 1 * flag
        x += 1 * flag
        for _ in range(height):
            numbers.append(matrix[x][y])
            x += 1 * flag
        x -= 1 * flag
        y -= 1 * flag
        flag *= -1
    numbers = numbers[-1:]+numbers[:-1]
    i = 0
    x = x1 - 1
    y = y1
    for _ in range(2):
        for _ in range(width):
            matrix[x][y] = numbers[i]
            i += 1
            y += 1 * flag
        y -= 1 * flag
        x += 1 * flag
        for _ in range(height):
            matrix[x][y] = numbers[i]
            i += 1
            x += 1 * flag
        x -= 1 * flag
        y -= 1 * flag
        flag *= -1


    return min(numbers), matrix

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))