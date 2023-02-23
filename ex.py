def solution(my_string, letter):
    answer = ''
    a = len(my_string)
    for i in range(a):
        if my_string[i] == letter:
            pass
        else:
            answer += my_string[i]
    return answer
            
print(solution('abcdef','d'))