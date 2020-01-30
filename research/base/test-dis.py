#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dis
import sys
import timeit
import textwrap

'''
Python代码分析工具之dis模块-分析字节码

Python代码分析工具之timeit模块-获取代码块执行时间
'''
dis.dis(lambda : dict())

dis.dis(lambda : {})

print(timeit.timeit("dict()"))
print(timeit.timeit("{}"))


print(timeit.timeit("dict()", number=10))
print(timeit.timeit("{}", number=10))