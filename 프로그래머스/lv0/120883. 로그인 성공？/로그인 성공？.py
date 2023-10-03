def solution(id_pw, db):
    pw_check = 0
    for d in db:
        if id_pw[0] == d[0]:
            if id_pw[1] == d[1]: return "login"
            else: pw_check = 1
    return "wrong pw" if pw_check==1 else "fail"