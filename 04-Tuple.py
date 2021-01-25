# 元组是 immutable （不可变的），一般可包含异质元素序列，通过解包（见本节下文）或索引访问（如果是 namedtuples，可以属性访问）。
# 列表是 mutable （可变的），列表元素一般为同质类型，可迭代访问。

empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)
len(singleton)
singleton

# 集合类型 集合是由不重复元素组成的无序容器
# 创建集合用花括号或 set() 函数
# 创建空集合只能用 set()，不能用 {}

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a

a - b                              # letters in a but not in b

a | b                              # letters in a or b or both

a & b                              # letters in both a and b

a ^ b                              # letters in a or b but not both
