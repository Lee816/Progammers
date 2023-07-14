def solution(myString):
    return ''.join(ch if ord(ch) > ord('l') else 'l' for ch in myString)