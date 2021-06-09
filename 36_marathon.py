def solution(participant, completion):
    answer = ''
    no_completion = []
    
    for name in participant:
        if name in completion:
            completion.remove(name)
        else:
            no_completion.append(name)
    answer = ' '.join(no_completion)
    return answer