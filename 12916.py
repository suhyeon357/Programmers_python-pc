def solution(s):
    answer = True
    s = s.lower()
    p_num = 0
    y_num = 0
    for i in range(len(s)):
        if s[i] == 'p':
            p_num += 1
        elif s[i] == 'y':
            y_num += 1

    if p_num != y_num:
        answer = False

    return answer

s = input()
print(solution(s))