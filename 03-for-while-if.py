# 遍历某个集合的同时修改该集合的内容，很难获取想要的结果。
# 要在遍历时修改集合的内容，应该遍历该集合的副本或创建新的集合：
users = {
    1 : "A",
    2 : "B"
}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    # print(user,status)
    if status == 'inactive':
        del users[user]
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# range()
# range(0,10,3) --> 0,3,6,9
# sum(range(4))
# list(range(4))
# 这种对象称为可迭代对象 iterable
print(range(10))    # range(0, 10)

# 1. 默认值参数     2. 关键字参数    3. 特殊参数
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 3.1. 位置或关键字参数

# 6. Lambda 表达式
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# 7. 循环的技巧 
# 5.6 https://docs.python.org/zh-cn/3/tutorial/datastructures.html
# 在字典中循环时，用 items() 方法可同时取出键和对应的值：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

#在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
