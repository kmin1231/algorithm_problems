DAYS_OF_WEEK = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# [NOTE] leap year
DAYS_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 2016.01.01.FRI
START_DAY_OFFSET =  4

def solution(a, b):
    total_days = sum(DAYS_IN_MONTH[:a-1]) + b
    answer = DAYS_OF_WEEK[(START_DAY_OFFSET + total_days) % 7]
    return answer