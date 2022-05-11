# 02.23 | 81 | Working with a deque

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print('rotate(3)                    ', dq)

dq.rotate(-4)
print('rotate(-4)                   ', dq)

dq.appendleft(-1)
print('appendleft(-1)               ', dq)

dq.extend([11, 22, 33])
print('extend([11, 22, 33])         ', dq)

dq.extendleft([10, 20, 30, 40])
print('extendleft([10, 20, 30, 40]) ', dq)
