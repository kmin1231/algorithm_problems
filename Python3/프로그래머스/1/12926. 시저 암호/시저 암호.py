alphabet = 'abcdefghijklmnopqrstuvwxyz'

def solution(s, n):
    answer = ''
    
    for char in s:
        if char == " ": answer += char
        elif char.islower():
            new_index = (alphabet.index(char) + n) % 26
            answer += alphabet[new_index]
        elif char.isupper():
            char = char.lower()
            new_index = (alphabet.index(char) + n) % 26
            answer += alphabet[new_index].upper()
    return answer