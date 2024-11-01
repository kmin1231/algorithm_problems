def solution(rank, attendance):
    students = dict()
    for i in range(len(rank)):
        if attendance[i] == True:
            students[i] =rank[i]
    students = dict(sorted(students.items(), key=lambda x:x[1]))
    selected = list(students.keys())[:3]
    a, b, c = selected[0], selected[1], selected[2]
    answer = 10000*a + 100*b + c
    return answer