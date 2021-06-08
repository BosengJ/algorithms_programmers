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
    for word in s_list:
        new_word = changeStr(word)
        ans_list.append(new_word)
        print(ans_list)
    answer = " ".join(ans_list)
    return answer