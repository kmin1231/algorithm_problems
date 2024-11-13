def solution(babbling):
    answer = 0
    terms = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        temp_word = word
        for term in terms:
            temp_word = temp_word.replace(term, " ", 1)
        if temp_word.strip() == "":
            answer += 1
    return answer