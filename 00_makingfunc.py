''' Sort
Min
Sum
Count'''

# Max 값 찾기
def searchMax(li):
    max_n = 0
    for n in li:
        if n > max_n:
            max_n = n
    return max_n

# Min 값 찾기
def searchMin(li):
    min_n = 0
    for i in range(len(li)):
        if i 


a_list = [1,2,3,4]
max_n = searchMax(a_list)
