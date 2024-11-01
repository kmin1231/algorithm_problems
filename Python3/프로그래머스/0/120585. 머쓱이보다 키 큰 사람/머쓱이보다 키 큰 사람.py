def solution(array, height):
    array.sort()
    temp = []
    for num in array:
        if num > height: temp.append(num)
    answer = len(temp)
    return answer