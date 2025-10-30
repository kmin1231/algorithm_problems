def solution(keymap, targets):
    answer = []

    for target in targets:
        total_presses = 0
        for char in target:
            min_presses = float('inf')  # infinity

            for key in keymap:
                if char in key:
                    presses = key.index(char) + 1   # the number of presses
                    min_presses = min(min_presses, presses)

            # cannot find target character
            if min_presses == float('inf'):
                total_presses = -1
                break

            total_presses += min_presses

        answer.append(total_presses)
    return answer