def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for x in range(i+1,len(numbers)):
            sum_num = numbers[i]+numbers[x]
            answer.append(sum_num)
    answer = list(set(answer))
    return answer