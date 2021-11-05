from collections import deque
a = [1,2,3]
queue = deque(a)
print(queue)
print(len(queue))
queue.popleft()

queue.popleft()

queue.popleft()
print(queue)
print(len(queue))