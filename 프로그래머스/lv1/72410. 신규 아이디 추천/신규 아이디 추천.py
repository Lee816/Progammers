def solution(new_id):
    noword = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id1=  new_id.lower()
    
    for i in range(len(noword)):
        if noword[i] in new_id1:
            new_id1 = new_id1.replace(noword[i],"")
            
    for i in range(len(new_id1)):
        if ".." in new_id1:
            new_id1 = new_id1.replace("..",".")
        new_id1 = new_id1.strip(".")
        if new_id1 == "":
            new_id1 = 'a'
            
    if len(new_id1) <= 2:
        new_id1 = new_id1 + new_id1[len(new_id1)-1]*(3-len(new_id1))
    elif len(new_id1) >= 16:
        new_id1 = new_id1[:15]
        new_id1 = new_id1.strip(".")
    
    answer = new_id1
                                                        
    return answer