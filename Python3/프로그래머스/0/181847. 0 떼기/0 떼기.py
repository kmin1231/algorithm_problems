def solution(n_str):
    for char in n_str:
        if (char == "0"):
            n_str = n_str[1:]
            answer = n_str
            continue
        else:
            answer = n_str
            break
    return answer