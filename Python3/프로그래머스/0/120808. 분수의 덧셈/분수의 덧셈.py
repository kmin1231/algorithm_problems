from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    
    divisor = gcd(numerator, denominator)
    
    if divisor == 1: pass
    else :
        numerator /= divisor
        denominator /= divisor

    answer = [numerator, denominator]
    return answer