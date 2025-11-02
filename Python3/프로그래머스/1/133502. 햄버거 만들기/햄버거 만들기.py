def solution(ingredient):
    stack = []   # LIFO
    count = 0    # the number of hamburgers

    for i in ingredient:
        stack.append(i)

        # ONLY the exact order: [bread (1) - vegetable (2) - meat (3) - bread (1)]
        # [NOTE] LIFO at the hamburger (pattern) level, NOT per individual ingredient
        if stack[-4:] == [1, 2, 3, 1]:
            count += 1
            del stack[-4:]

    return count