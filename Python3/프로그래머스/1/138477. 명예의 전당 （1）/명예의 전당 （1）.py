def solution(k, score):
    hall_of_fame = []
    answer = [] # worst scores

    for s in score:
        hall_of_fame.append(s)
        hall_of_fame.sort(reverse=True)

        if len(hall_of_fame) > k:
            hall_of_fame = hall_of_fame[:k]

        answer.append(hall_of_fame[-1]) # worst score
    return answer