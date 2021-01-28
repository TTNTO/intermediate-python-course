# 操作系统接口
import os
import shutil
# 文件通配符
import glob
# 命令行参数
import sys
import argparse
# 错误输出重定向和程序终止

# 字符串模式匹配
import re
# 数学
import math
import random
import statistics
# 互联网访问
from urllib.request import urlopen
import smtplib
# 日期和时间
from datetime import date
# 数据压缩
import zlib
# 性能测试
from timeit import Timer
# 质量控制
# doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
# unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:
 
