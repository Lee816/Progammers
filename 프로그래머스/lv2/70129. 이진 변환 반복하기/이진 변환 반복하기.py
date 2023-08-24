def solution(s):
    answer = [0,0]
    
    while 1:
        answer[0] += 1
        answer[1] += list(s).count('0')
        
        if list(s).count('1') == 1:
            break
        else:
            s = bin(list(s).count('1'))[2:]
    
    return answer

    