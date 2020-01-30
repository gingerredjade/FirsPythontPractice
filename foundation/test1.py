#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Python注释: 双引号 or 三个单引号 or 一个井号
'''


'''打印操作'''
"定义打印函数"


def print_your_name(name):
    print("jianghy hadoop test,your name is", name)
    print("\r\t")
    return "%s, is a good student." % name
    # Python2.x使用如下，注意编码
    # print ("jianghy hadoop test,your name is"),name.decode("utf-8")
    # return ("%s, is a good student.") % name.decode("utf-8")


"调用打印函数"
print('===================')
print(print_your_name('zhangsan'))
print('===================')
print(print_your_name('李四'))
print('===================')


'''常用的数据结构'''
# Java常用数据结构:hashmap，array，set

# Python:hashmap-->dict -->{}
# Python:array-->list   -->[]
# Python:set-->set      -->()

# dict字典
"color是个变量，等于一个字典"
color = {"red":0.2,"green":0.4, "blue": 0.4}
print(color)
print(color['red'])
print(color['green'])

# list列表
color_list = ['red','blue','green','yellow']
print(color_list)
print(color_list[2])

# set集合
"set不能有重复元素"
a_set = set()
a_set.add('111')
a_set.add('222')
a_set.add('333')
a_set.add('111')
print(a_set)


'''条件判断语句'''
# if
a = 1
if a > 0:
    print('a gt 0')
elif a == 0:
    print('a eq 0')
else:
    print('a lt 0')

# for 一般对于数组操作，也可对字典、集合操作
# # 创建一个列表并追加元素
a_list = []
a_list.append('111')
a_list.append('333')
a_list.append('555')
a_list.append('222')
a_list.append('444')

for value in a_list:
    print(value)

##
b_dict = {}
b_dict['aaa'] = 1
b_dict['bbb'] = 2
b_dict['ddd'] = 3
b_dict['ccc'] = 4
b_dict['eee'] = 5

for value in b_dict:
    "这里的value值包含字典的key，不包含其对应的value"
    print(value)
for key, value in b_dict.items():
    "其输出顺序并不按照存储顺序输出的。而是针对key做了一个哈希取模"
    print(key + "====>" + str(value))

##
c_set = set()
c_set.add('a')
c_set.add('b')
c_set.add('c')
c_set.add('d')
c_set.add('e')

for value in c_set:
    "set背后也有哈希做了操作，输出顺序并不是add顺序"
    print(value)

# # 复杂一点
sum = 0
for value in range(1,11):
    sum += value
print(sum)


# while
cnt = 2
while cnt > 0:
    print('i love python!')
    cnt -= 1

# # print dual 输出双数
"注意：Python不支持i++"
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)


'''字符串的简单处理'''
# len()可以对字符串、字典、列表、set进行长度的计算
str = 'abcdefg'
print(len(str))
"[2:5]中的2表示从下标2开始获取，极限是5"
print(str[2:5])

# 字母大小写转换
str1 = 'AbcDEf'
print(str1)
print(str1.lower())
print(str1.upper())


'''异常处理 exception'''
# Java: try ... catch
# except Exception相当于捕捉了所有异常
try:
    a = 6
    b = a / 0
except Exception as e:
        print (Exception, ":", e)
# 注意：2.x按照如下写
# try:
#     a = 6
#     b = a / 0
# except Exception, e:
#         print Exception, ":", e


## IO异常
try:
    print('1111')
    fh = open('testfile', 'r')
    print('2222')
except IOError as e:
    print('3333====', e)
else:
    print('4444')
    fh.close()


'''import module'''
import math
# 求2的3次方
print(math.pow(2, 3))
print(math.floor(4.9))
print(round(4.9))


# 将有序数组随机化洗牌处理
import random
items = [1, 2, 3, 4, 5, 6]
random.shuffle(items)
print(items)

# 输出随机数：输出0-3之间的数字
a = random.randint(0, 3)
print(a)

# sample就是抽样,在字符串里随机抽样,要指定抽样数据的个数
s_list = random.sample('acdfg', 3)
print(s_list)

''''''

''''''





