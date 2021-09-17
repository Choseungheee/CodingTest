def solution(n):
    answer = 0 # 답
    s = 0 # 연속된 숫자의 sum
    i = 1 # 더할 값
    start = 1 # i의 시작 값
    while True:
        s += i
        i += 1
        if s >= n:
            if s == n:
                answer += 1
            start += 1
            i = start
            s = 0
        if start == n:
            return answer + 1