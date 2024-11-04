def solution(array):
    count = dict()
    for num in array:
        if num in count: count[num] += 1
        else : count[num] = 1
    sorted_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    answer = sorted_count[0][0]
    if len(sorted_count) >= 2:
        if sorted_count[0][1] == sorted_count[1][1]: answer = -1
    return answer