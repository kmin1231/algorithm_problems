def solution(s):
    answer = 0
    command = s.split(" ")
    for i in range(len(command)):
        if command[i] == "Z": answer -= int(command[i-1])
        else : answer += int(command[i])    
    return answer