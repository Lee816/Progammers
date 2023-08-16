def solution(s):
    answer = []
    for ch in s:
        if ch == '(':
            answer.append(ch)
        elif ch == ')':
            if answer and answer[-1] == '(':
                answer.pop()
            else:
                return False
    return not(answer)
                