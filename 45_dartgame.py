def letsSplit(li):
    # string10을 Q로 치환
    for i in range(len(li)):
        if (i < len(li)-1) and li[i] == '1' and li[i+1] == '0':
            q_dartResult = li[:i] + 'Q'
            if (i+1) != (len(li)-1):
                q_dartResult += li[(i+2):]
            break
        else:
            q_dartResult = li
    q_dartResult_split = list(q_dartResult)
    
    # Q를 다시 10으로 치환
    dartResult_split = []
    for ch in q_dartResult_split:
        if ch != 'Q':
            dartResult_split.append(ch)
        else:
            dartResult_split.append('10')
    return dartResult_split

def SDT(li):
    SDT = {'S':1, 'D':2, 'T':3}
    SDT_score_list = []
    for i in range(len(li)):
        if li[i] in "SDT":
            SDT_score = int(li[i-1]) ** SDT[li[i]]
            SDT_score_list.append(SDT_score)
        if li[i] in "*#":
            SDT_score_list.append(li[i])
    return SDT_score_list

def starSharp(li):
    final_list = []
    for score in li:
        final_list.append(score)
        
        # '#'이 있는 단계의 점수
        if score == '#':
            final_list[-1] = int(final_list[-1]) * (-1)
        # '*'이 있는 단계의 점수
        elif score == '*':
            final_list[-1] = int(final_list[-1]) * 2
            if len(final_list) > 1:
                final_list[-2] = int(final_list[-2]) * 2
    return final_list
        
#         # '*','#'가 없는 단계의 점수
#         if (i < (len(li)-1)) and (str(li[i]) not in "*#") and (str(li[i+1]) not in "*#"):
#             final_list.append(li[i])
            
#         # '*','#'이 없는 stage03 단계의 점수
#         elif (i == len(li)-1) and (str(li[i]) not in "*#"):
#             final_list.append(li[i])
        
#         # stage01단계에서 '*'이 있는 경우
#         elif (i<2) and (li[i] == '*'):
#             final_list.append(int(li[i-1])*2)
        
#         # stage02, stage03에서 '*'이 있는 경우
#         elif li[i] == '*':
#             final_list[-1] = int(final_list[-1])*2
#             final_list.append(int(li[i-1])*2)
        
#         # '#'이 있는 경우
#         elif li[i] =='#':
#             final_list.append(int(li[i-1])*(-1))
    # return final_list
    
def solution(dartResult):
    
    dartResult_split = letsSplit(dartResult)
    print(dartResult_split)
    
    SDT_score_list = SDT(dartResult_split)
    print(SDT_score_list)
    
    final_list = starSharp(SDT_score_list)
    print(final_list)
    
    answer = 0
    for score in final_list:
        answer += int(score)
    return answer