# (최대)힙 구조 만들기
def heapify():
    for i in range(1, N):
        c = i
        while c > 0:
            root = (c - 1) // 2
            if numbers[c] > numbers[root]:
                numbers[c], numbers[root] = numbers[root], numbers[c]
            c = root
    return

# (최소)힙 구조 만들기
def minHeapify():
    for i in range(1,N):
        c = i
        while c > 0:
            root = (c - 1) // 2
            if numbers[c] < numbers[root]:
                numbers[root], numbers[c] = numbers[c], numbers[root]
            c = root
    return


# 힙 정렬하기(오름차순)
def heap_sort():
    for i in range(N - 1, -1, -1):  # n
        # 맨 앞과 맨 뒤를 교환! ( 가장 큰 수를 뒤로 보낸다. 그리고 그 가장 큰 수는 FIX!!!! )
        numbers[0], numbers[i] = numbers[i], numbers[0]

        # 힙구조가 이상해졌으므로 다시 힙구조로 바꾼다.  # logn
        root, c = 0, 1
        while c < i:
            c = root * 2 + 1
            if c < i - 1 and numbers[c] < numbers[c + 1]:
                c += 1

            if c < i and numbers[c] > numbers[root]:
                numbers[c], numbers[root] = numbers[root], numbers[c]
            root = c
    return


# numbers = [2, 7, 3, 4, 5, 6, 1]
numbers = [42,22,4,58,1,5,0,5]
N = len(numbers)
# minHeapify()
# print(numbers)
heapify()
print(numbers)
heap_sort()
print(numbers)

# numbers.pop()
# print(numbers)