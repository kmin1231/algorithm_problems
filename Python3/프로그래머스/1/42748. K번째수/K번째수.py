def solution(array, commands):
    answer = []

    for i, j, k in commands:
        slice = array[i-1:j]
        sorted_slice = sorted(slice)
        answer.append(sorted_slice[k-1])

    return answer