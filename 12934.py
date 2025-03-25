# 실행시간 초과
def solution(n):
    answer = -1
    for i in range(1, n+1):
        if i*i == n:
            answer = (i+1)**2
    return answer

# 제곱근 구하는 문제여서 n까지의 모든 수를 제곱하여 for문사용
# -> 시간초과
# **0.5 사용 -> 각 수를 제곱하는게 아니라 루트씌우기
def solution_2(n):
    if int(n**0.5) == n**0.5:
        return (n**0.5+1)**2
    else:
        return -1