import math
from collections import defaultdict

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_rate = fees
    
    in_time = dict()
    total_time = defaultdict(int)
    
    for record in records:
        time_str, car_num, in_out = record.split()
        time_min = time_to_minutes(time_str)
        
        if in_out == "IN":
            in_time[car_num] = time_min
        else:
            accumulated = time_min - in_time[car_num]
            total_time[car_num] += accumulated
            del in_time[car_num]
            
    # no 'OUT'
    end_of_day = time_to_minutes("23:59")
    for car_num, enter_time in in_time.items():
        accumulated = end_of_day - enter_time
        total_time[car_num] += accumulated
    
    # car_num ascending
    answer = []
    for car_num in sorted(total_time):
        time = total_time[car_num]
        if time <= basic_time:
            fee = basic_fee
        else:
            fee = basic_fee + math.ceil((time - basic_time) / unit_time) * unit_rate
        answer.append(fee)
    return answer