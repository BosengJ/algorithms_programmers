'''
가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
※ 공지 - 2021년 10월 20일 테스트케이스가 추가되었습니다.
'''

# 리스트 내 elments를 3번 반복하는 문자열로 만들기
def tripleWord(li):
    tri_li =[]
    for num in li:
        tri_num = num * 3
        tri_li.append(tri_num)
    return tri_li

# 내림차순 함수
def LargeToSmall(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

# 새번 반복한 문자열에서 다시 원상복구 시키는 함수
def returnNum(li):
    n_li = []
    for num in li:
        N = len(num) // 3
        tmp = num[:N]
        n_li.append(tmp)
    return n_li

def solution(numbers):
    # numbers의 elments를 str형으로 바꿔준다
    str_nums = list(map(str,numbers))
    
    # numbers의 원소는 1,000 이하이므로 3자리 이하로 비교하기 위해 각 원소를 3번 반복해준다
    triple_nums = tripleWord(str_nums)
    
    # 큰 수 -> 작은 수 정렬해준다
    sorted_nums = LargeToSmall(triple_nums)
    
    # 숫자를 원상복구 시킨다
    return_nums = returnNum(sorted_nums)
    
    # elements를 합쳐주어 답을 구한다
    answer = str(int(''.join(return_nums)))
    # print(str_nums)
    # print(triple_nums)
    # print(sorted_nums)
    # print(return_nums)
    # print(answer)
    return answer

# test case

# numbers = [6, 10, 2]	
# 정답 "6210"

# numbers = [3, 30, 34, 5, 9]	
# 정답 "9534330"

numbers = [87,878]

a = solution(numbers)
print(a)