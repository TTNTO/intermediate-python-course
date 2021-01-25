# 转义字符 \
print("doesn\'t")
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并：
# 拆分长字符串时，这个功能特别实用：
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错：