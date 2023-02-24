def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for i in reserve_set: # 1,3,5

        if i - 1 in lost_set:
            lost_set.remove(i - 1)

        elif i + 1 in lost_set:
            lost_set.remove(i + 1)
    
    answer = n - len(lost_set)
    return answer



n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution(n, lost, reserve))