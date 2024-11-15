def solution(s):
    numbers = [int(num) for num in s.split(" ")]
    ordered = sorted(numbers)
    answer = " ".join([str(ordered[0]), str(ordered[-1])])
    return answer