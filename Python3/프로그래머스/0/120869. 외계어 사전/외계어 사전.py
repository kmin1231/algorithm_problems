def solution(spell, dic):
    for word in dic:
        if all(word.count(char) == 1 for char in spell):
            answer = 1
            break
        else: answer = 2
    return answer