from collections import Counter

def solution(participant, completion):

    # [NOTE] duplicate names may exist
    diff = Counter(participant) - Counter(completion)
    incomplete = list(diff)[0]

    return incomplete