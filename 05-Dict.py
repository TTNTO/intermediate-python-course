# 对字典执行 list(d) 操作，返回该字典中所有键的列表
# 按插入次序排列（如需排序，请使用 sorted(d)
# 检查字典里是否存在某个键，使用 in 关键字。
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel)

sorted(tel)

'guido' in tel

'jack' not in tel
# dict() 构造函数可以直接用键值对序列创建字典：
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# 字典推导式可以用任意键值表达式创建字典：
{x: x**2 for x in (2, 4, 6)}

# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷:
dict(sape=4139, guido=4127, jack=4098)
