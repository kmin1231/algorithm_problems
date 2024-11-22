def solution(s):
    answer = ''
    words = s.split(" ")
    new_list = []
    for word in words:
        new = ''
        for i in range(len(word)):
            if (i%2 == 0): new += word[i].upper()
            else : new += word[i].lower()
        new_list.append(new)
    answer = " ".join(new_list)
    return answer