def solution(ingredient):
    answer = 0
    item = []
    for x in ingredient:
        item.append(x)
        if len(item) > 3:
            if item[-1] == 1:
                if item[-2] == 3:
                    if item[-3] == 2:
                        if item[-4] == 1:
                            item.pop()
                            item.pop()
                            item.pop()
                            item.pop()
                            answer += 1
    return answer