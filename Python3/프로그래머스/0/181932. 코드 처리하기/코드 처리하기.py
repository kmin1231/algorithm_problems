def solution(code):
    answer = ''
    mode = 0
    count = len(code)
    for i in range(count):
        if (mode == 0):
            if (code[i] == '1'): mode = 1
            else:
                if (i%2 == 0):
                    answer += code[i] 
                else: continue
        else:
            if (code[i] == '1'): mode = 0
            else:
                if (i%2 == 1):
                    answer += code[i] 
                else: continue
    if answer == '':
        answer = 'EMPTY' 
    return answer