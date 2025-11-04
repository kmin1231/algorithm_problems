def solution(s):
    stack = []

    for char in s:
        # [NOTE] check if stack is NOT empty to avoid IndexError!
        if stack and (stack[-1] == char): stack.pop()
        else: stack.append(char)
    answer = 1 if not stack else 0
    return answer