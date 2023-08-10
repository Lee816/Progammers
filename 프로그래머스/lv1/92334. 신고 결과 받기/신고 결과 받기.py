def solution(id_list, report, k):
    num = [0 for i in range(len(id_list))]
    set_report = set(report)
    answer = [0 for i in range(len(id_list))]

    for report_id in set_report:
        user1 = report_id.split()[1]
        for i in range(len(id_list)):
            if id_list[i]==user1:
                num[i] = num[i] + 1
                
    for i in range(len(num)):
        if num[i] >=  k:
            for j in range(len(answer)):
                reportset = id_list[j]+" "+id_list[i]
                if reportset in set_report:
                    answer[j] = answer[j] + 1
            
    return answer