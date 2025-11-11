def solution(nums):
    num_types = len(set(nums))
    max_pick = len(nums) // 2

    # [NOTE] NO need to generate all combinations!
    answer =  min(num_types, max_pick)

    return answer