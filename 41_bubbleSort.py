def bubbleSort(li):
    list_len = len(li)
    for i in range(list_len-1):
        for j in range(list_len-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1] , li[j]
    return li