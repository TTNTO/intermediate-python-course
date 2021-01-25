squares = [1, 4, 9, 16, 25]

squares + [36, 49, 64, 81, 100]

#与 immutable 字符串不同, 列表是 mutable 类型
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64

# methods https://docs.python.org/zh-cn/3/tutorial/datastructures.html
cubes.append(216)

# 1. 用作堆栈
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()

# 2. 列表作为队列使用
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue                           # Remaining queue in order of arrival

# 3. 列表推导式
squares = list(map(lambda x: x**2, range(10)))
# 等价于
squares = [x**2 for x in range(10)]

# 4. 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]