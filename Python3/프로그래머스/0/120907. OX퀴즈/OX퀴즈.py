def solution(quiz):
    answer = []
    for eqn in quiz:
        eqn = eqn.split(" ")
        a, b, exp = int(eqn[0]), int(eqn[2]), int(eqn[4])
        if eqn[1] == "+":
            result = "O" if (a + b == exp) else "X"
        else:
            result = "O" if (a - b == exp) else "X"
        answer.append(result)
    return answer