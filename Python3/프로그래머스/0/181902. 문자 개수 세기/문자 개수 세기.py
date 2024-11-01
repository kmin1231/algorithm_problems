import string
keys = list(string.ascii_uppercase) + list(string.ascii_lowercase)

def solution(my_string):
    answer = []
    count = {key: 0 for key in keys}
    for char in my_string:
        count[char] += 1
    answer = list(count.values())
    return answer