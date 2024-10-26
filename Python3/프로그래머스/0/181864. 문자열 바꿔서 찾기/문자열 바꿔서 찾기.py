def solution(myString, pat):
    flipped = ''
    for char in myString:
        if (char == "A"): flipped += char.replace("A", "B")
        elif (char == "B"): flipped += char.replace("B", "A")
    if (pat in flipped): answer = 1
    else: answer = 0
    return answer