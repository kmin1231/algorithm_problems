def solution(people, limit):
    people.sort()   # from lightest to heaviest

    left_idx, right_idx = 0, len(people) - 1
    count = 0   # the number of boats

    # (greedy algorithm) try to pair the lightest with the heaviest
    # [NOTE] should include equality sign to count the LAST person
    while left_idx <= right_idx:
        if people[left_idx] + people[right_idx] <= limit:
            left_idx += 1
        right_idx -= 1
        count += 1
    return count