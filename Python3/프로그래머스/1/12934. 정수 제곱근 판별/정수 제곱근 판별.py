def solution(n):
    sqrt = n**0.5
    if sqrt.is_integer(): return (sqrt+1)*(sqrt+1)
    else : return -1