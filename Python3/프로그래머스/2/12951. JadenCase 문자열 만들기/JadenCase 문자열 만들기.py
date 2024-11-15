def solution(s):
    answer = ""
    result = []
    for chunk in s.split(" "):
        result.append(chunk.capitalize())
    answer = " ".join(result)
    return answer