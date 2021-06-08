def changeStr(p):
    change_str = ""
    for i in range(len(p)):
        if i % 2 == 0:
            new_str = p[i].upper()
        else:
            new_str = p[i].lower()
        change_str += new_str
    return change_str
            
def solution(s):
    s_list = s.split()
    answer = ""
    ans_list = []
    for p in s_list:
        new_para = changeStr(p)
        ans_list.append(new_para)
    answer = " ".join(ans_list)
    return answer

s = "try hello world"
a = 'i love you'
b = 'i LOvE yOU'
c = 'I LOVE YOU'
d = 'i Am jEONg Ga rAm'

print(solution(s))
print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))