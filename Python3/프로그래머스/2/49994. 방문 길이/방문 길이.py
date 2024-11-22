def solution(dirs):
    answer = 0
    pos = [0, 0]
    save = set()  # NO duplication

    for cmd in dirs:
        old_pos = tuple(pos)
        
        if cmd == "U":
            if (pos[1]+1) <= 5: pos[1] += 1
        elif cmd == "D":
            if (pos[1]-1) >= -5: pos[1] -= 1
        elif cmd == "R":
            if (pos[0]+1) <= 5: pos[0] += 1
        else:  # "L"
            if (pos[0] -1) >= -5: pos[0] -= 1
            
        new_pos = tuple(pos)
        if old_pos != new_pos:
            save.add((old_pos, new_pos))
            save.add((new_pos, old_pos))  # opposite direction

    answer = len(save)//2
    return answer