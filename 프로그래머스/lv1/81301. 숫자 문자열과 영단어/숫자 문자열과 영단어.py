def solution(s):
    
    number = { 'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    s = s.lower()
    
    keys = list(number.keys())
    values = list(number.values())
    
    for i in range(len(keys)):
        if keys[i] in s:
            s = s.replace(keys[i],str(values[i]))
    
    answer = int(s)
    return answer