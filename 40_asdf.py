def checkPrimeNum(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    return True

def solution(nums):
    sum_three_nums = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum_num = nums[i] + nums[j] + nums[k]
                sum_three_nums.append(sum_num)
    sum_three_nums = set(sum_three_nums)
    
    answer = 0
    for i in sum_three_nums:
        if checkPrimeNum(i) == True:
            answer += 1
    return answer