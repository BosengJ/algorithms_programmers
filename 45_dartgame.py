def letsSplit(dartResult):
    for i in range(len(dartResult)):
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            q_dartResult = dartResult[:i] + 'Q' + dartResult[(i+2):]
            break
        else:
            q_dartResult = dartResult
    q_dartResult_split = list(q_dartResult)
    
    dartResult_split = []
    for ch in q_dartResult_split:
        if ch != 'Q':
            dartResult_split.append(ch)
        else:
            dartResult_split.append('10')
    return dartResult_split

def SDT(dartResult_split):
    score_list = []
    for i in range(len(dartResult_split)):
        if dartResult_split[i] == 'S':
            score_list.append(int(dartResult_split[i-1]))
        if dartResult_split[i] == 'D':
            score_list.append(int(dartResult_split[i-1])**2)
        if dartResult_split[i] == 'T':
            score_list.append(int(dartResult_split[i-1])**3)
        if (dartResult_split[i] == '*') or (dartResult_split[i] == '#'):
            score_list.append(dartResult_split[i])
    return score_list

def starSharp(sdt_score_list):
    final_score = []
    for i in range(len(sdt_score_list)):
        final_score.append(sdt_score_list[i])
        if sdt_score_list[i] == '#':
            final_score = final_score[:-2]
            final_score.append(int(sdt_score_list[i-1])*(-1))  
            
        if (i<2) and (sdt_score_list[i] == '*'):
            final_score = []
            final_score.append(int(sdt_score_list[i-1])*(2))
    
    ffinal_score  = []
    for i in range(len(final_score)):
        if final_score[i] == '*':
            ffinal_score = ffinal_score[:-2]
            ffinal_score.append(int(final_score[i-2])*2)
            ffinal_score.append(int(final_score[i-1])*2)
        else:
            ffinal_score.append(final_score[i])
    return ffinal_score
     
def solution(dartResult):
    dartResult_split = letsSplit(dartResult)
    print(dartResult_split)
    
    sdt_score_list = SDT(dartResult_split)
    print(sdt_score_list)
    
    final_score_list = starSharp(sdt_score_list)
    print(final_score_list)
    
    answer = 0
    for score in final_score_list:
        answer += int(score)

    return answer