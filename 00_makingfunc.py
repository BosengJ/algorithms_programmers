# Max 값 찾기
def searchMax(li):
    max_n = 0
    for n in li:
        if n > max_n:
            max_n = n
    return max_n

# Min 값 찾기
def searchMin(li):
    for i in range(len(li)):
        if i == 0:
            min_n = li[i]
        elif li[i] < min_n:
            min_n = li[i]
    return min_n

# BubbleSort 오름차순
def ascending(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li

# BubbleSort 내림차순
def descending(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li
            
# sum
def sumList(li):
    sum_num = 0
    for num in li:
        sum_num += num
    return sum_num

# count
def countElements(li):
    dict_li = dict(zip(li,'0'*len(li)))
    for num in li:
        for k in dict_li.keys():
            if num == k:
                dict_li[k] = int(dict_li[k]) + 1
    return dict_li

