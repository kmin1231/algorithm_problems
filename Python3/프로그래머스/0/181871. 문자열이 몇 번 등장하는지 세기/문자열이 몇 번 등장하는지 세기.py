def solution(myString, pat):
    count = 0
    length = len(pat)
    for i in range(len(myString) - length + 1):
        if myString[i:i+length] == pat: count += 1
        else: continue
    return count