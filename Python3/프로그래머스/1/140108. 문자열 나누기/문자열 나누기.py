def solution(s):
    count = 0
    x = ''
    same, diff = 0, 0

    for ch in s:
        # initialization
        if not x: x = ch

        if ch == x: same += 1
        else: diff += 1

        if same == diff:
            count += 1

            # reinitialization
            x = ''
            same, diff = 0, 0

    # [NOTE] in case 's' ends before same == diff
    if x: count += 1

    return count