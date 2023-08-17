def solution(s):
    return ''.join([ch.upper() if not ch.isdigit() and s[i-1] == ' ' or i==0 else ch.lower() for i,ch in enumerate(s)])