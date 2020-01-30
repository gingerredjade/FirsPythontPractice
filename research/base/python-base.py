#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
import dis

'''
list
'''
# 列表中同事含有int和string类型的元素
testlist = [1, 2, 'hello', 'world']
print(testlist)
# 切片[1:3]包头不包尾，索引从0开始
print(testlist[1:3])

# 元组中同时含有int和String类型的元素
tup = ('jason', 22)
print(tup)

'''
dict
'''
# 字典创建-基础
dict1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
dict2 = dict({'name': 'jason', 'age':20, 'gender': 'male'})
dict3 = dict([('name', 'jason'), ('age', 20),('gender', 'male')])
dict4 = dict(name='jason', age=20, gender='male')
print(dict1 == dict2 == dict3 == dict4)

# Python3.7以后插入有序变为字典的特性，构造新字典的方式有如下
# 字典创建-double star
dict11 = {'name': 'jason', 'age': 20, 'gender': 'male'}
dict12 = {'hobby': 'swim', **dict11}
dict13 = {**dict11, 'hobby': 'swim'}
print('current dict11 is ', dict11)
print('current dict12 is ', dict12)
print('current dict13 is ', dict13)

# 字典创建-update函数
dict14 = {'hobby': 'swim'}
dict14.update(dict11)
dict11.update(dict14)
print('current dict14 is ', dict14)
print('current dict11 is ', dict11)


'''
set
'''
# 集合创建方式
set1 = {1, 2, 3}
set2 = set([1, 2, 3])
print("is set1 == set2? ", set1 == set2)


'''
string
Python的字符串是不可变的（immutable）
'''
str1 = 'hello'
for char in str1:
    print(char)


# Option A
str2 = 'H' + str1[1:]
# Option B
str2 = str2.replace('h', 'H')
print(str2)

# 加法操作符'+='字符串拼接方法，打破了字符串不可变的特性
s = ''
for n in range(0, 100000):
    s += str(n)
print(s)

# 字符串拼接-string内置join函数
list30 = []
for n in range(0, 100000):
    list30.append(str(n))
list30 = ''.join(list30)
print(list30)

# 字符串分割
def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding data
    :param namespace:
    :param table:
    :return:
    """

    path = 'hive://ads/training_table'
    namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
    table = path.split('//')[1].split('/')[1]  # 返回'training_table'
    data = query_data(namespace, table)
    return data


'''
pprint
'''
# pprint美观打印数据结构
data = [{
    "l1": {
        "l1_1": [
            "l1_1_1",
            "l1_1_2"
        ],
        "l1_2": {
            "l1_2_1": 121
        }
    },
    "l2": {
        "l2_1": "null",
        "l2_2": "true",
        "l2_3": {}
    }
}]
print(data)
pprint(data)




