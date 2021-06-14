'''이상한 문자 만들기

문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, 
solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"

입출력 예 설명
"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 
각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 
"TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.'''

def changeStr(word):
    change_str = ""
    for i in range(len(word)):
        if i % 2 == 0:
            new_str = word[i].upper()
        else:
            new_str = word[i].lower()
        change_str += new_str
    return change_str
            
def solution(s):
    # s_list = s.split(' ')
    # split 안쓰고 구현하기
    ch = ""
    split_list = []
    for i in range(len(s)):
        if s[i] != ' ':
            ch = ch + s[i]
        else:
            split_list.append(ch)
            ch = ""
        if i == len(s)-1:
            split_list.append(ch)
        print(ch)
    print(split_list)
    answer = ""
    ans_list = []
    for word in split_list:
        new_word = changeStr(word)
        ans_list.append(new_word)
    answer = " ".join(ans_list)
    return answer