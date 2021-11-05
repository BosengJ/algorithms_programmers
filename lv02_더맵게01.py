'''
더 맵게
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
'''

# Test case
'''
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
'''

# (최소)힙 구조 만들기
def minHeapify(li):
    N = len(li)
    for i in range(1,N):
        c = i
        while c > 0:
            root = (c - 1) // 2
            if li[c] < li[root]:
                li[root], li[c] = li[c], li[root]
            c = root
    return li

# (최대)힙 구조 만들기
def heapify(li):
    N = len(li)
    for i in range(1, N):
        c = i
        while c > 0:
            root = (c - 1) // 2
            if li[c] > li[root]:
                li[c], li[root] = li[root], li[c]
            c = root
    return li


# 힙 정렬하기(오름차순)
def heap_sort(li):
    N = len(li)
    for i in range(N - 1, -1, -1):  # n
        # 맨 앞과 맨 뒤를 교환! ( 가장 큰 수를 뒤로 보낸다. 그리고 그 가장 큰 수는 FIX!!!! )
        li[0], li[i] = li[i], li[0]

        # 힙구조가 이상해졌으므로 다시 힙구조로 바꾼다.  # logn
        root, c = 0, 1
        while c < i:
            c = root * 2 + 1
            if c < i - 1 and li[c] < li[c + 1]:
                c += 1

            if c < i and li[c] > li[root]:
                li[c], li[root] = li[root], li[c]
            root = c
    return li

# 주어진 문제대로 새로운 스코빌 지수를 만들어내는 함수
def calScoville(li):
    num = li[0] + (li[1] * 2)
    del li[0]
    del li[0]
    li.append(num)
    return li

# main 함수
def solution(scoville, K):
    answer = 0

    # 배열 속 모든 스코빌 지수가 K 이상이 되었을 때 멈추거나
    # 원소가 1개 남았는데 이 마저도 K 이상이 아니라면 반복문을 멈춘다
    while True:
        heapify_sco = heapify(scoville)         # 배열을 정렬해주고
        print(heapify_sco)
        sort_sco = heap_sort(heapify_sco)
        if sort_sco[0] > K:
            break
        if len(sort_sco) == 1:
            return -1
        scoville = calScoville(sort_sco)        # 주어진 대로 계산해준다
        answer += 1                             # 카운트 1회 늘린다
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
a = solution(scoville, K)
print(a)


