'''모의고사
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예

answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]

입출력 예 설명

입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.'''

def madMath(answer_list,num_math,answers):
    if num_math > len(answer_list):
        p = num_math // len(answer_list)
        q = num_math % len(answer_list)
        answer_list = (answer_list * p) + (answer_list[:q])
        
    elif num_math < len(answer_list):
        answer_list = answer_list[:num_math]
        
    score = 0
    for (i,j) in zip(answers,answer_list):
        if i == j:
            score += 1
    return score

def solution(answers):
    num_math = len(answers)
    answer_list01 = [1,2,3,4,5]
    answer_list02 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_list03 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score01 = madMath(answer_list01,num_math,answers)
    score02 = madMath(answer_list02,num_math,answers)
    score03 = madMath(answer_list03,num_math,answers)
    score_list = [score01,score02,score03]
    
    max_score = 0
    for i in score_list:
        if i > max_score:
            max_score = i
            
    answer = []
    for i in range(len(score_list)):
        if max_score == score_list[i]:
            answer.append(i+1)
    
    return answer