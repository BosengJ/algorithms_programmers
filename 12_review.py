def solution(ab,s):
    return sum(ab[i] if s[i] == True else ab[i]*(-1) for i in range(len(ab)))


ab = [4,7,12]	
s = [True,False,True]	
print(solution(ab,s))