def solution(polynomial):
    term0, term1 = 0, 0
    terms = polynomial.split(" + ")
    for term in terms:
        if "x" in term:
            if term == "x": term1 += 1
            else : term1 += int(term[:-1])
        else : term0 += int(term)
        
    if (term1 == 0) and (term0 == 0): answer = "0"
    elif (term1 == 0) or (term0 == 0):
        if term1 == 0: answer = f"{term0}"
        elif term0 == 0: answer = f"{term1}x" if term1 != 1 else "x"
    else:
        if term1 == 1: answer = f"x + {term0}"
        else: answer = f"{term1}x + {term0}"
    return answer