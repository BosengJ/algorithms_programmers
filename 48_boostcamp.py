'''함수 구현
자연수가 들어있는 배열 arr가 매개변수로 주어집니다. 배열 arr안의 숫자들 중에서 앞에 있는 숫자들부터 뒤에 중복되어 나타나는 숫자들 중복 횟수를 계산해서 배열로 return 하도록 solution 함수를 완성해주세요. 만약 중복되는 숫자가 없다면 배열에 -1을 채워서 return 하세요.

ex) 
arr = [1,2,3,3,3,3,4,4]
return [4,2]

arr = [3,2,4,4,2,5,2,5,5]
return [3,2,3]

arr = [3,5,7,9,1]
return [-1]'''

def solution(arr):
    arr_dict = dict(zip(arr,'0'*len(arr)))
    for n in arr:
        if n in arr_dict:
            arr_dict[n] = int(arr_dict[n]) + 1
    answer = []
    for v in arr_dict.values():
        if v > 1:
            answer.append(v)
        else:
            answer = [-1]
    
    return answer

# arr = [1,2,3,3,3,3,4,4]
# return [4,2]

# arr = [3,2,4,4,2,5,2,5,5]
# return [3,2,3]

# arr = [3,5,7,9,1]
# return [-1]

