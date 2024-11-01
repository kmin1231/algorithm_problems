def solution(picture, k):
    rows, cols = len(picture), len(picture[0])
    answer = []
    for i in range(rows):
        row = []
        for j in range(cols):
            for x in range(k):
                row.append(picture[i][j])
        for y in range(k):
            answer.append(''.join(row))
    return answer