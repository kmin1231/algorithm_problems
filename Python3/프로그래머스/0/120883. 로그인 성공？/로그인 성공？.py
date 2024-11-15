def solution(id_pw, db):
    username = id_pw[0]
    password = id_pw[1]
    for info in db:
        if info[0] == username:
            if info[1] == password:
                answer = "login"
                break
            else : answer = "wrong pw"
            break
        else: answer = "fail"
    return answer