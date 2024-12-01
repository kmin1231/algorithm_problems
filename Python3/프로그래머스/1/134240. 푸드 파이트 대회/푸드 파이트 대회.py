def solution(food):
    answer = ''
    for i in range(1, len(food)):
        n = food[i] - 1 if (food[i]%2) != 0 else food[i]
        nfood = str(i) * n
        answer = answer[:len(answer)//2] + nfood + answer[len(answer)//2:]
    answer = answer[:len(answer)//2] + "0" + answer[len(answer)//2:]
    return answer