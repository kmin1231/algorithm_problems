num_dict = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e',
            '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}

def solution(age):
    answer = ''
    age_str = str(age)
    age_list = list(age_str)
    for num in age_list:
        answer += num_dict[num]
    return answer