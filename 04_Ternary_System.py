def solution(n):
    reverse_third =''
    while n > 0:
        q,r = divmod(n,3)
        reverse_third += str(r)
        n = q
        answer = int(reverse_third,3)
    return answer