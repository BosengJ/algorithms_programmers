arr = [[1,2],[1,2],[3,4],[1,2]]

answer = []
for i in range(len(arr)):
    if (i>0) and (arr[i] in answer):
        cnt = answer.count(arr[i])
        arr[i].append(cnt)
        answer.append(arr[i]) 

    else:
        answer.append(arr[i]) 
print(answer)

