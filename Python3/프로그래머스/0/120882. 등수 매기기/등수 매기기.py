def solution(score):
    answer = []
    avg_list = []
    for num in score:
        avg = (num[0]+num[1])/2
        avg_list.append(avg)
    ordered = sorted(avg_list, reverse=True)
    for i in avg_list:
        answer.append(ordered.index(i)+1)
    return answer