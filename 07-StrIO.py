# 要使用 格式化字符串字面值 ，请在字符串的开始引号或三引号之前加上一个 f 或 F
# 在此字符串中，你可以在 { 和 } 字符之间写可以引用的变量或字面值的 Python 表达式。
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# 当你不需要花哨的输出而只是想快速显示某些变量以进行调试时，
# 可以使用 repr() or str() 函数将任何值转化为字符串。
s = 'Hello, world.'
str(s)
repr(s)
del s

# 
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

# 手动格式化字符串
# 字符串对象的 str.rjust() 方法通过在左侧填充空格来对给定宽度的字段中的字符串进行右对齐
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

# %（求余）可用于字符串格式化
print('The value of pi is approximately %5.3f.' % math.pi)