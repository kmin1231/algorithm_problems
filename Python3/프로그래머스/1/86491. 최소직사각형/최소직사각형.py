def solution(sizes):

    # considers rotation
    rotated = [(max(w, h), min(w, h)) for w, h in sizes]
    
    # maximum width & height
    max_w = max(w for w, h in rotated)
    max_h = max(h for w, h in rotated)

    # maximum wallet size
    max_size = max_w * max_h

    return max_size