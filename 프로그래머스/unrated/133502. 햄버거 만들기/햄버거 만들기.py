def solution(ingredient):
    answer = 0
    item = []
    for x in ingredient:
        item.append(x)
        if len(item) > 3:
            if item[-4:] == [1,2,3,1]:
                answer += 1
                for _ in range(4):
                    item.pop()
    return answer