def solution(myString):
    temp = myString.split("x")
    while "" in temp: temp.remove("")
    temp.sort()
    answer = temp
    return answer