'''피보나치 수
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
* n은 1이상, 100000이하인 자연수입니다.

입출력 예
n	return
3	2
5	5
입출력 예 설명
피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.'''

def solution(n):
    cnt = 2
    fibonacci_li = [0,1]
    while True:
        if n == 2:
            break
        else:
            tmp = []
            tmp.append(fibonacci_li[-1])
            tmp.append(sum(fibonacci_li))
            fibonacci_li = tmp[:]
            cnt += 1
        if cnt == n:
            break
            
    fibonacci_num = 0
    for n in fibonacci_li:
        fibonacci_num += n

    answer = fibonacci_num % 1234567
    return answer



# 시간초과
# def solution(n):
#     dict_fib = {}
#     for i in range(1,n):
#         if (i == 1) or (i == 2):
#             dict_fib[i] = [1]
#         else:
#             dict_fib[i] = dict_fib[i-1] + dict_fib[i-2]

#     fibonacci_li = dict_fib[n-1] + dict_fib[n-2]
#     fibonacci_num = len(fibonacci_li)
#     answer = fibonacci_num % 1234567
#     return answer



# 시간초과
# def check_only_zero_one(li):
#     for n in li:
#         if (n == 0) or (n == 1):
#             continue
#         else:
#             return False
#     return True

# def solution(n):
#     fibonacci = [n]
#     if n >= 2:
#         while True:
#             new_fibonacci = []
#             for n in fibonacci:
#                 if n > 2:
#                     new_fibonacci.append(n-1)
#                     new_fibonacci.append(n-2)
#                 elif (n == 1) or (n == 2):
#                     new_fibonacci.append(1)
#             if check_only_zero_one(new_fibonacci) == True:
#                 break
#             else:
#                 fibonacci = new_fibonacci[:]
    
#     fibonacci_num = 0
#     for n in new_fibonacci:
#         fibonacci_num += n
    
#     answer = fibonacci_num % 1234567

#     return answer