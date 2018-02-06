# dir(object)

# if type(1) == type(2) :
#     print("same type")
# if type(1) != type("asd"):
#     print("unsame type")
# if isinstance(1, int):
#     print("isinstance")

# i = 10
# print(hex(i))   #16进制
# print(oct(i))   #8进制
# print(bin(i))   #2进制

# a = 1
# print(a.bit_length())
# b = 1024
# print(b.bit_length())

# 小数
# import decimal
# from decimal import Decimal
#
# decimal.getcontext().prec = 4
# print(Decimal("0.01") + Decimal("0.02"))

# 分数
# from fractions import Fraction
# x = Fraction(3, 6)
# print(x)
# x = Fraction("0.25")
# print(x)

# set
# s = set([1,2,3,4,5])
# b = set([9,8,7,6,5])
# print(s | b)             # 并集
# print(s.union(b))        # 并集
# print(s & b)             # 交集
# print(s.intersection(b)) # 交集
# print(s - b)             # 差集
# print(s.difference(b))   # 差集
# print(s ^ b)             # 对称差集（在s或者b中，不会同时存在）
# print(s.symmetric_difference(b))
#
# s.add("s")
# print(s)
#
# print(2 in s)
# print(2 not in s)
# print(s.issubset(b))
# print(set([2]).issubset(s))
# print(s.issuperset(set([2])))
#
# ss = s.copy()
# print(ss)
# s.discard('s')
# print(s)
#
# ss.clear()
# print(ss)
#
# print({x for x in s})
# print({x**2 for x in [1,2,3,4]})
# print({x for x in 'text'})


# frozenset集合
# a = set([1,3,4])
# b = set()
# # b.add(a)    # error， set是不可哈希类型，不可作为字典的key
# b.add(frozenset(a))
# print(b)

# bool布尔类型
# print(type(True))
# print(isinstance(False, int))   # bool属于int类型
# print(True == 1)                # True 等于 1
# print(True == 2)

# 动态类型
# a = [1]
# b = [1]
# print(a is b)
# c = d = [1,2]
# print(c is d)

# 常见字符串
# print("s\np\tss")
# print("""fun""")    # 三重引号，一般用于函数说明
# print(r'\temp')     # Raw字符串，不会进行转义
# print(b'Spam')      # Python3中的字节字符串
# print(u'Spam')      # Python2.6中的Unicode字符串
# print("a {1} {0} {2} b".format(1,2,3))
#
# s = 'spam'
# for x in s :
#     print(x)
# print({x for x in s})
#
# print(','.join(['1','2','3']))

# 内置str处理函数
# str = "StringObject dd"
# print(str.upper())
# print(str.lower())
# print(str.swapcase())   # 大小写转换
# print(str.capitalize()) # 首字母大写
# print(str.title())      # 每个单词首字母大写
#
# print(str.ljust(200))
# print(str.find('t'))
# print(str.find('t',1,2))
#
# print(str.replace("Ob", "OOb"))
# print(str.strip())
# print(str.strip('d'))
# print(str.startswith("Str"))
# print(str.endswith("dd"))
#
# print(str.isalnum())
# print(str.isalpha())
# print(str.isupper())
# print(str.islower())


# 索引，分片
# s = [1,2,3,4,5,6,7,8,9]
# print(s[1])
# print(len(s) - 1)
# print(s[-1])
# print(s[1:3])
# print(s[1:])
# print(s[:-1])
# print(s[1:10:2])

# 字符串转换工具
print(int("11"))
print(str(11))
print(ord('a'))
print(chr(97))
















