def solution(arr, divisor):
    ans = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            ans.append(arr[i])
    ans.sort()
    if len(ans) == 0:
        ans.append(-1)
    return ans