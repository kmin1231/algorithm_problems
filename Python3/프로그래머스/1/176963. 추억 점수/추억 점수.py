def solution(name, yearning, photo):
    answer = []
    for pic in photo:
        point = 0
        for mem in pic:
            if mem in name:
                idx = name.index(mem)
                point += yearning[idx]
            else : point += 0
        answer.append(point)
    return answer