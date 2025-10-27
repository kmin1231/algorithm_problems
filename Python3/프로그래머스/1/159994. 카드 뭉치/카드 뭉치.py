def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0

    for word in goal:
        # [NOTE] check if 'idx1' and 'idx2' are within range
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1

        else:
            return "No"
    return "Yes"