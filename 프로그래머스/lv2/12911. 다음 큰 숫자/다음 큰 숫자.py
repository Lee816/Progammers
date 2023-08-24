def solution(n):
    answer = n
    while 1:
        answer += 1
        if list(str(bin(n))).count('1') == list(str(bin(answer))).count('1'):
            return answer
        
    # bin() 값에 .count() 사용가능