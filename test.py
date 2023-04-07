import math

'''类和对象'''
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f'这个学生的姓名是：{self.name},年龄是{self.age}')
#
#     def study(self,score,rank):
#         self.score = score
#         self.rank = rank
#         print(f'这个学生的成绩是：{score},排名是{self.rank}')
#
#
# Stu1 = Student('张三',19)
# Stu1.study(750,1)


''' 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：'''
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#   print(k, v)


'''在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：'''
# for i, v in enumerate(['tic', 'tac', 'toe']):
#   print(i, v)


'''同时遍历两个或更多的序列，可以使用 zip() 组合：'''
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(f'What is your {q}?  It is {a}.')

'''
str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
'''
# repr() 的参数可以是 Python 的任何对象
#  repr() 函数可以转义字符串中的特殊字符
# hello = 'hello, runoob\n'
# hellos = repr(hello)
# print(hellos)

# range(num) --  到num-1
# for i in range(1,10):
#     print(i)

# str = input("请输入：");
# print ("你输入的内容是: " + "我喜欢  " + str)


'''
+	加 - 两个对象相加	a + b 输出结果 31
-	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
*	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
/	除 - x 除以 y	b / a 输出结果 2.1
%	取模 - 返回除法的余数	b % a 输出结果 1
**	幂 - 返回x的y次幂	a**b 为10的21次方
//	取整除 - 向下取接近商的整数
'''


'''Python 质数判断'''
# # 用户输入数字
# num = int(input("请输入一个数字: "))
#
# # 质数大于 1
# if num > 1:
#     # 查看因子
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "不是质数")
#             print(i, "乘于", num // i, "是", num)
#             break
#     else:
#         print(num, "是质数")
#
# # 如果输入的数字小于或等于 1，不是质数
# else:
#     print(num, "不是质数")


''' 通过用户输入数字计算阶乘'''
# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))
# factorial = num
#
# # 查看数字是负数，0 或 正数
# if num < 0:
#     print("抱歉，负数没有阶乘")
# elif num == 0:
#     print("0 的阶乘为 1")
# else:
#     for i in range(num-1 ,1,-1 ):
#         factorial = factorial * i
#     print("%d 的阶乘为 %d" % (num, factorial))


'''for循环打印是左闭右开[ , )'''
# for i in range(1,10):
#     print(i,end=' ')
# print('\n')
# for i in range(10,1,-1):
#     print(i,end=' ')


''' Python 斐波那契数列实现'''
# # 获取用户输入数据
# nterms = int(input("你需要几项？"))
#
# # 第一和第二项
# n1 = 0
# n2 = 1
# count = 2
#
# # 判断输入的值是否合法
# if nterms <= 0:
#     print("请输入一个正整数。")
# elif nterms == 1:
#     print("斐波那契数列：")
#     print(n1)
# else:
#     print("斐波那契数列：")
#     print(n1, ",", n2, end=" , ")
#     while count < nterms:
#         nth = n1 + n2
#         print(nth, end=" , ")
#         # 更新值
#         n1 = n2
#         n2 = nth
#         count += 1


'''Python 检测用户输入的数字是否为阿姆斯特朗数'''
#
# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))
#
# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))
#
# # 检测
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10  #取除以10后的整数部分
#
# # 输出结果
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print(num, "不是阿姆斯特朗数")


# # 二次方程式 ax**2 + bx + c = 0
# # a、b、c 用户提供，为实数，a ≠ 0
#
# # 导入 cmath(复杂数学运算) 模块
# import cmath
#
# a = float(input('输入 a: '))
# b = float(input('输入 b: '))
# c = float(input('输入 c: '))
#
# # 计算
# d = (b ** 2) - (4 * a * c)
#
# # 两种求解方式
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
#
# print('结果为 {0} 和 {1}'.format(sol1, sol2))

'''求两个数的最大公约数'''
# # 定义一个函数
# def hcf(x, y):
#     """该函数返回两个数的最大公约数"""
#
#     for i in range(1, min(x,y) + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))


'''Python生成日历'''
# # 引入日历模块
# import calendar
#
# # 输入指定年月
# yy = int(input("输入年份: "))
# mm = int(input("输入月份: "))
#
# # 显示日历
# print(calendar.month(yy, mm))
# # print(calendar.prcal(yy))

'''Python 使用递归斐波那契数列  (效率很低捏'''
# def recur_fibo(n):
#     """递归函数
#     输出斐波那契数列"""
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
#
# # 检查输入的数字是否正确
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i))

'''Python 获取昨天日期'''
# # 引入 datetime 模块
# import datetime
#
# def getYesterday():
#     yesterday = datetime.date.today() + datetime.timedelta(-1)
#     return yesterday
# # 输出
# print(getYesterday())


'''Python 约瑟夫生者死者小游戏'''

'''
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''

# people={}
# for x in range(1,31):
#     people[x]=1
# # print(people)
# check=0
# i=1
# j=0
# while i<=31:
#     if i == 31:
#         i=1
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             i+=1
#             continue
#         else:
#             check+=1
#             if check == 9:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue

'''列表的旋转'''
# def rverseArray(arr, start, end):
#     while (start < end):
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp
#         start += 1
#         end = end - 1
#
#
# def leftRotate(arr, d):
#     n = len(arr)
#     rverseArray(arr, 0, d - 1)
#     rverseArray(arr, d, n - 1)
#     rverseArray(arr, 0, n - 1)
#
#
# def printArray(arr):
#     for i in range(0, len(arr)):
#         print(arr[i], end=' ')
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 2)
# printArray(arr)


'''Python 移除列表中重复的元素'''

# list_1 = [1, 2, 1, 4, 6]
# print(list(set(list_1)))
#
# # 删除两个列表中重复的元素
# # 在以下实例中，两个列表中同时存在的元素会被删除。
#
#
# list_1 = [1, 2, 1, 4, 6]
# list_2 = [7, 8, 2, 1]
#
# print(list(set(list_1) ^ set(list_2)))



'''Python 将字符串作为代码执行'''

'''
Document 对象参考手册 Python3 实例

给定一个字符串代码，然后使用 exec() 来执行字符串代码。

实例 1：使用内置方法 exec()
'''

# def exec_code():
#     LOC = """
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact = fact*i
#     return fact
# print(factorial(5))
# """
#     exec(LOC)
#
# exec_code()

'''
Python 合并字典
'''

# def Merge(dict1, dict2):
#     return (dict1.update(dict2))
#
#
# # 两个字典
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
#
# # 返回  None
# print(Merge(dict1, dict2))
#
# # dict1 合并了 dict2
# print(dict1)

'''使用 **，函数将参数以字典的形式导入'''

# def Merge(dict1, dict2):
#     res = {**dict1, **dict2}
#     return res
#
# # 两个字典
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = Merge(dict1, dict2)
# print(dict3)



'''小蓝每天都锻炼身体正常情况下'''

# import datetime
#
# start = datetime.date(2000, 1, 1)
# end = datetime.date(2020, 10, 1)
# deltadays = datetime.timedelta(days=1)
# ans = 0
#
# while end >= start:
#     if start.day == 1 or start.weekday() == 0:
#         ans += 2
#     else:
#         ans += 1
#     start += deltadays
# print(ans)

'''求一个数的因子'''
# l=[]
# n=2021041820210418
# for i in range(1,int(n**0.5)+1):
#     if(n % i == 0):
#         l.append(i)
#         l.append(int(n/i))
# print(sorted(l))


'''请问，有多少个既约分数，分子和分母都是 1 到 2020之间的整数'''
# import math
# num=0
# for x in range(1,2021):
#     for y in range(1, 2021):
#         if(math.gcd(x,y)==1):
#             num+=1
# print(num)


# l=[1,1,1]
# for i in range(1,20190322):
#   add=l[-1]+l[-2]+l[-3]
#   l.append(add)
# print(l[-1])

# n=int(input())
# sum=0
# for i in range(1,n+1):
#     li=str(i)
#
#     for j in li:
#         if(j=='2' or j=='0' or j=='1' or j=='9'):
#             sum+=i
#             break
# print(sum)

# num=0
# for i in range(1,2019):
#     for j in range(1,2019-i):
#         k = 2019-i-j
#         if('2' not in str(i) and '2' not in str(j)and '2' not in str(k) and '4' not in str(i) and '4' not in str(j) and '4' not in str(k) and i+j+k==2019 and i<j and j<k ):
#                 num+=1
# print(num)


# arr=[]
# N,K=map(int,input().split())
# for i in range(1,N+1):
#     A=int(input())
#     arr.append(A)
#
# num=0
# for j in range(0,N):
#     sum=0
#     for k in range(j,N):
#         sum+=arr[k]
#         if((sum%K)==0):
#             num+=1
# print(num)

'''给定一个长度为 N 的数组 A，请你先从小到大输出它的每个元素，再从大到小输出它的每个元素'''

# n=input()
# a=list(map(int,input().split()))
# print(a)
# print(*sorted(a))
# print(*sorted(a,reverse=True))
#
# a=[4,3,7,8,1,2]
# print(sorted(a))
# print(*a)
# print(*sorted(a))
# print(*sorted(a,reverse=True))



# l='''VLPWJVVNNZSWFGHSFRBCOIJTPYNEURPIGKQGPSXUGNELGRVZAG
# SDLLOVGRTWEYZKKXNKIRWGZWXWRHKXFASATDWZAPZRNHTNNGQF
# ZGUGXVQDQAEAHOQEADMWWXFBXECKAVIGPTKTTQFWSWPKRPSMGA
# BDGMGYHAOPPRRHKYZCMFZEDELCALTBSWNTAODXYVHQNDASUFRL
# YVYWQZUTEPFSFXLTZBMBQETXGXFUEBHGMJKBPNIHMYOELYZIKH
# ZYZHSLTCGNANNXTUJGBYKUOJMGOGRDPKEUGVHNZJZHDUNRERBU
# XFPTZKTPVQPJEMBHNTUBSMIYEGXNWQSBZMHMDRZZMJPZQTCWLR
# ZNXOKBITTPSHEXWHZXFLWEMPZTBVNKNYSHCIQRIKQHFRAYWOPG
# MHJKFYYBQSDPOVJICWWGGCOZSBGLSOXOFDAADZYEOBKDDTMQPA
# VIDPIGELBYMEVQLASLQRUKMXSEWGHRSFVXOMHSJWWXHIBCGVIF
# GWRFRFLHAMYWYZOIQODBIHHRIIMWJWJGYPFAHZZWJKRGOISUJC
# EKQKKPNEYCBWOQHTYFHHQZRLFNDOVXTWASSQWXKBIVTKTUIASK
# PEKNJFIVBKOZUEPPHIWLUBFUDWPIDRJKAZVJKPBRHCRMGNMFWW
# CGZAXHXPDELTACGUWBXWNNZNDQYYCIQRJCULIEBQBLLMJEUSZP
# RWHHQMBIJWTQPUFNAESPZHAQARNIDUCRYQAZMNVRVZUJOZUDGS
# PFGAYBDEECHUXFUZIKAXYDFWJNSAOPJYWUIEJSCORRBVQHCHMR
# JNVIPVEMQSHCCAXMWEFSYIGFPIXNIDXOTXTNBCHSHUZGKXFECL
# YZBAIIOTWLREPZISBGJLQDALKZUKEQMKLDIPXJEPENEIPWFDLP
# HBQKWJFLSEXVILKYPNSWUZLDCRTAYUUPEITQJEITZRQMMAQNLN
# DQDJGOWMBFKAIGWEAJOISPFPLULIWVVALLIIHBGEZLGRHRCKGF
# LXYPCVPNUKSWCCGXEYTEBAWRLWDWNHHNNNWQNIIBUCGUJYMRYW
# CZDKISKUSBPFHVGSAVJBDMNPSDKFRXVVPLVAQUGVUJEXSZFGFQ
# IYIJGISUANRAXTGQLAVFMQTICKQAHLEBGHAVOVVPEXIMLFWIYI
# ZIIFSOPCMAWCBPKWZBUQPQLGSNIBFADUUJJHPAIUVVNWNWKDZB
# HGTEEIISFGIUEUOWXVTPJDVACYQYFQUCXOXOSSMXLZDQESHXKP
# FEBZHJAGIFGXSMRDKGONGELOALLSYDVILRWAPXXBPOOSWZNEAS
# VJGMAOFLGYIFLJTEKDNIWHJAABCASFMAKIENSYIZZSLRSUIPCJ
# BMQGMPDRCPGWKTPLOTAINXZAAJWCPUJHPOUYWNWHZAKCDMZDSR
# RRARTVHZYYCEDXJQNQAINQVDJCZCZLCQWQQIKUYMYMOVMNCBVY
# ABTCRRUXVGYLZILFLOFYVWFFBZNFWDZOADRDCLIRFKBFBHMAXX'''
# li=l.split('\n')
# sum=0
# for i in range(30):
#     for j in range(50):
#         for x in range(i+1,30):
#             if(li[i][j]<li[x][j] and i<x):
#                 sum+=1
#         for y in range(j+1,50):
#             if(li[i][j]<li[i][y] and j<y):
#                 sum+=1
#         for m in range(0,i):
#             for n in range(j + 1,50):
#                 if(li[i][j]<li[m][n] and i-m==n-j):
#                     sum+=1
#         for a in range(i+1, 30):
#             for b in range(j + 1, 50):
#                 if (li[i][j] < li[a][b] and a - i == b - j):
#                     sum += 1
#         for o in range(i+1,30):
#             for p in range(0,j):
#                 if(li[i][j]<li[o][p] and o-i==j-p):
#                     sum+=1
#
# print(sum)


# n=int(input())
# li=list(map(int,input().split()))
# sum=0
# while(len(li)>1):
#     li.sort()
#     sum+=li[0]+li[1]
#     cost=li[0]+li[1]
#     for i in range(0,len(li)-2):
#         li[i]=li[i+2]
#     for j in range(2):
#         li.pop()
#     li.append(cost)
# print(sum)

# # 从用户输入中读取一个整数n
# n = int(input())
#
# # 如果n的值在1到200之间，则执行以下操作
# if n >= 1 and n <= 200:
#     # 从用户输入中读取一个空格分隔的整数列表，并将其转换为整数类型
#     li = list(map(int, input().split()))
#
#     # 对列表进行排序
#     li = sorted(li)
#
#     # 遍历整个列表
#     for i in range(len(li)):
#         # 如果列表中的某个元素的值大于或等于10000或小于或等于-10000，则从列表中删除该元素
#         if li[i] >= 10000 or li[i] <= -10000:
#             del li[i]
#
#     # 打印经过删除操作后的列表
#     print(li)

"""
判断一个数是否为素数
"""
# def is_prime(n):
#
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def count(li):  # 求此子串的f值
#     s = []
#     num = 0
#     for i in range(len(li)): #遍历li
#         if (li[i] not in s):
#             s.append(li[i])
#             num += 1
#     return num


# sum = 0
# S = input()
# for j in range(len(S)): #遍历S每一个字母
#     k=len(S)          #最后一个字母的下标
#     while(j<k):
#         # print(S[j:k])
#         sum+=count(S[j:k])
#         k-=1
        
# print(sum)

# n=3.345534
# print("数字保留四个小数是{:.4f}".format(n))


'''
模块datetime的一些用法    来源:https://zhuanlan.zhihu.com/p/208291869
datetime类可以看作date和time类的合体，其包含了这两个类中的全部参数
'''
# import datetime

'''date类包含三个参数，分别为year，month，day，返回格式为year-month-day'''

# today=datetime.date(year=2002,month=11,day=27)
# print(today)
# print('date对象的年份:', today.year)    

# print('date对象的月份:', today.month)   

# print('date对象的日:', today.day)  

# print("date对象的struct_time结构为：",today.timetuple())

# print("返回当前公历日期的序数:",today.toordinal())   #  与fromordinal函数作用相反

# print("当前日期为星期(其中：周一对应0):{}".format(today.weekday()))

# print("当前日期为星期(其中：周一对应1):{}".format(today.isoweekday()))

# print("当前日期的年份、第几周、周几(其中返回为元组):",today.isocalendar())

# print("以ISO 8601格式‘YYYY-MM-DD’返回date的字符串形式：",today.isoformat())

# print("返回一个表示日期的字符串(其格式如：Mon Aug 31 00:00:00 2020):",today.ctime())

# print("指定格式为：",today.strftime("%Y/%m/%d"))

# print("替换后的日期为：",today.replace(2019,9,29))

'''
结果如下：

date对象的年份: 2020
date对象的月份: 8
date对象的日: 31
date对象的struct_time结构为： time.struct_time(tm_year=2020, tm_mon=8, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=244, tm_isdst=-1)
返回当前公历日期的序数: 737668
当前日期为星期(其中：周一对应0):0
当前日期为星期(其中：周一对应1):1
当前日期的年份、第几周、周几(其中返回为元组): (2020, 36, 1)
以ISO 8601格式‘YYYY-MM-DD’返回date的字符串形式： 2020-08-31
返回一个表示日期的字符串(其格式如：Mon Aug 31 00:00:00 2020): Mon Aug 31 00:00:00 2020
指定格式为： 2020/08/31
替换后的日期为： 2019-09-29
'''

# now = datetime.datetime(2020,8,31,12,10,10)

# print("年为：",now.year)

# print("月为：",now.month)

# print("日为：",now.day)

# print("小时为：",now.hour)

# print("分钟为：",now.minute)

# print("秒数为：",now.second)

# print('当前日期为:', now.date() )

# print('当前时间:', now.time() )

# print("返回struct_time为",now.timetuple())   #  和date一样

# print("返回UTC的struct_time为",now.utctimetuple())

# print("返回的公历序列数为：",now.toordinal())   #  和date一样

# print("返回标准日期格式为：",now.isoformat())   #  和date一样

# print("返回的周几(1表示周一)：",now.isoweekday())    #  和date一样

# print("返回的周几(0表示周一)：",now.weekday())    #  和date一样  

# print("now.isocalendar():", now.isocalendar())  #  和date一样

# print("now.ctime():",now.ctime())   #  和date一样

# print("格式化时间为：",now.strftime('%Y/%m/%d %H:%M:%S'))   #  把日期按照format指定的格式进行格式化

# print(datetime.datetime.strptime("2020/12/29 8:8:00",'%Y/%m/%d %H:%M:%S'))     #   将字符串格式转换为日期格式

'''
结果如下：

年为： 2020
月为： 8
日为： 31
小时为： 12
分钟为： 10
秒数为： 10
当前日期为: 2020-08-31
当前时间: 12:10:10
返回struct_time为 time.struct_time(tm_year=2020, tm_mon=8, tm_mday=31, tm_hour=12, tm_min=10, tm_sec=10, tm_wday=0, tm_yday=244, tm_isdst=-1)
返回UTC的struct_time为 time.struct_time(tm_year=2020, tm_mon=8, tm_mday=31, tm_hour=12, tm_min=10, tm_sec=10, tm_wday=0, tm_yday=244, tm_isdst=0)
返回的公历序列数为： 737668
返回标准日期格式为： 2020-08-31T12:10:10
返回的周几(1表示周一)： 1
返回的周几(0表示周一)： 0
now.isocalendar(): (2020, 36, 1)
now.ctime(): Mon Aug 31 12:10:10 2020
格式化时间为： 2020/08/31 12:10:10
2020-12-29 08:08:00
'''

'''timedelta类'''

# now = datetime.date.today()

# before_5_date = now + datetime.timedelta(days=-5)

# print("now date is:",now)   # 表示现在的日期

# print("\n")

# print("before five days date is:",before_5_date)   # 表示五天前的日期

# now_time = datetime.datetime.now()

# print(now_time)

# after_5_hours_10_minutes = now_time + datetime.timedelta(hours=5,minutes=10)

# print(after_5_hours_10_minutes)


'''
结果如下：
now date is: 2020-08-31
before five days date is: 2020-08-26
2020-08-31 13:14:53.862049
2020-08-31 18:24:53.862049
'''


'''
2020 年春节期间，有一个特殊的日期引起了大家的注意：2020 年 2 月 2 日。因为如果将这个日期按 “yyyymmdd” 的格式写成一个 8 位数是 20200202，
恰好是一个回文数。我们称这样的日期是回文日期。

有人表示 20200202 是 “千年一遇” 的特殊日子。对此小明很不认同，因为不到 2 年之后就是下一个回文日期：20211202 即 2021 年 12 月 2 日。

也有人表示 20200202 并不仅仅是一个回文日期，还是一个 ABABBABA 型的回文日期。对此小明也不认同，因为大约 100 年后就能遇到下一个 ABABBABA 型的
回文日期：21211212 即 2121 年 12 月 12 日。算不上 “千年一遇”，顶多算 “千年两遇”。

给定一个 8 位数的日期，请你计算该日期之后下一个回文日期和下一个 ABABBABA 型的回文日期各是哪一天。

输入描述
输入包含一个八位整数 N，表示日期。
对于所有评测用例，10000101≤≤8999123110000101≤N≤89991231，保证 N 是一个合法日期的 8 位数表示。

输出描述
输出两行，每行 1 个八位数。第一行表示下一个回文日期，第二行表示下一个 ABABBABA 型的回文日期。
'''
# import datetime
# N=str(input())
# y=int(N[0:4])
# m=int(N[4:6])
# d=int(N[6:8])
# the_day=datetime.date(y,m,d)
# while(True):
#     the_day+=datetime.timedelta(days=1)
#     strthe_day=str(the_day).replace('-','')
#     if(strthe_day[::-1]==strthe_day):
#         huiwenday=the_day
#         while(True):
#             huiwenday+=datetime.timedelta(days=1)
#             strhuiwenday=str(huiwenday).replace('-','')
#             A=strhuiwenday[0]
#             B=strhuiwenday[1]
#             if(strhuiwenday[2]==A and strhuiwenday[5]==A and strhuiwenday[7]==A and strhuiwenday[3]==B and strhuiwenday[4]==B and strhuiwenday[6]==B):
#                 break
#         break

# print(strthe_day)
# print(strhuiwenday)


'''
数学老师给小明出了一道等差数列求和的题目。但是粗心的小明忘记了一 部分的数列，只记得其中 
N 个整数。现在给出这 N 个整数，小明想知道包含这 N 个整数的最短的等差数列有几项？
'''
'''思路：求最小公差dm，则最短的等差数列项数为(（数列最大-数列最小）/dm)+1'''
# N=int(input())
# li=list(map(int,input().split()))
# li.sort()
# d=[]
# for i in range(len(li)-1):
#     d.append(li[i+1]-li[i])
# d.sort()
# dm=d[0]
# print(int((((li[-1]-li[0])/dm)+1)))


'''你有一架天平和 N 个砝码，这 N 个砝码重量依次是 1,2,⋅⋅⋅,W1​,W2​,⋅⋅⋅,WN​。
请你计算一共可以称出多少种不同的重量？ 注意砝码可以放在天平两边。'''


# N=int(input())
# li=list(map(int,input().split()))
# set1=set()
# set1.add(0)
# for i in li:
#     for j in list(set1):
#         set1.add(i+j)
#         set1.add(abs(i-j))
# print(len(set1)-1)
        


'''设有 n 个人围坐在圆桌周围，现从某个位置 k 上的人开始报数，报数到 m 的人就站出来。
下一个人，即原来的第 m+1 个位置上的人，又从 1开始报数，再报数到 m 的人站出来。
依次重复下去，直到全部的人都站出来为止。试设计一个程序求出这 n 个人的出列顺序。'''


# n,k,m=map(int,input().split())
# li=[]
# for i in range(1,n+1):
#     li.append(i)
# point=k-1
# while(len(li)>0):
#     point=(point+m-1)%len(li)
#     print(li[point])
#     li.pop(point)
    
'''小蓝要把一个字符串中的字母按其在字母表中的顺序排列。

例如，LANQIAO 排列后为 AAILNOQ。'''
    
# li=str('WHERETHEREISAWILLTHEREISAWAY')
# li=sorted(li)
# str=''.join(li)
# print(str)


'''汉字的字形存在于字库中，即便在今天，16 点阵的字库也仍然使用广泛。
点阵的字库把每个汉字看成是16×16 个像素信息。并把这些信息记录在字节中。
一个字节可以存储 8 位信息，用 32 个字节就可以存一个汉字的字形了。 
把每个字节转为 2 进制表示，1 表示墨迹，0 表示底色。每行 2 个字节，一共 
16 行'''

# data = """4 0 4 0 4 0 4 32 -1 -16 4 32 4 32 4 32 4 32 4 32 8 32 8 32 16 34 16 34 32 30 -64 0 
# 16 64 16 64 34 68 127 126 66 -124 67 4 66 4 66 -124 126 100 66 36 66 4 66 4 66 4 126 4 66 40 0 16 
# 4 0 4 0 4 0 4 32 -1 -16 4 32 4 32 4 32 4 32 4 32 8 32 8 32 16 34 16 34 32 30 -64 0 
# 0 -128 64 -128 48 -128 17 8 1 -4 2 8 8 80 16 64 32 64 -32 64 32 -96 32 -96 33 16 34 8 36 14 40 4 
# 4 0 3 0 1 0 0 4 -1 -2 4 0 4 16 7 -8 4 16 4 16 4 16 8 16 8 16 16 16 32 -96 64 64 
# 16 64 20 72 62 -4 73 32 5 16 1 0 63 -8 1 0 -1 -2 0 64 0 80 63 -8 8 64 4 64 1 64 0 -128 
# 0 16 63 -8 1 0 1 0 1 0 1 4 -1 -2 1 0 1 0 1 0 1 0 1 0 1 0 1 0 5 0 2 0 
# 2 0 2 0 7 -16 8 32 24 64 37 -128 2 -128 12 -128 113 -4 2 8 12 16 18 32 33 -64 1 0 14 0 112 0 
# 1 0 1 0 1 0 9 32 9 16 17 12 17 4 33 16 65 16 1 32 1 64 0 -128 1 0 2 0 12 0 112 0 
# 0 0 0 0 7 -16 24 24 48 12 56 12 0 56 0 -32 0 -64 0 -128 0 0 0 0 1 -128 3 -64 1 -128 0 0 



'''我们知道第一个质数是 2第二个质数是 3第三个质数是 5……请你计算第 2019 个质数是多少？'''


# def is_prime(num):
#     for i in range(2,num):
#         if(num%i == 0):
#             return False
#     return True


# sum=0
# for i in range(2,99999):
#     if(is_prime(i)):
#         sum+=1
#         if(sum==2019):
#             print(i)
#             break


'''小蓝发现，他将 1 至 1000000007 之间的不同的数与 2021 相乘后再求除以 1000000007 
的余数，会得到不同的数。 小蓝想知道，能不能在 1 至 1000000007 之间找到一个数，与 2021
 相乘后 再除以1000000007 后的余数为 999999999。如果存在，请在答案中提交这个数；
 如果不存在，请在答案中提交 0。'''

# for i in range(1,1000000008):
#     if((i*2021)%1000000007==999999999):
#         print(i)


'''有 N 棵灌木整齐的从左到右排成一排。爱丽丝在每天傍晩会修剪一棵灌 木, 让灌木的高度变为 0 厘米。
爱丽丝修剪灌木的顺序是从最左侧的灌木开始, 每天向右修剪一棵灌木。当修剪了最右侧的灌木后, 
她会调转方向, 下一天开 始向左修剪灌木。直到修剪了最左的灌木后再次调转方向。然后如此循环往复。
灌木每天从早上到傍晩会长高 1 厘米, 而其余时间不会长高。在第一天的 早晨, 所有灌木的高度都是 0 厘米。
爱丽丝想知道每棵灌木最高长到多高。'''

# N=int(input())
# tree=[]
# for i in range(N):
#     tree.append(0)
# for j in range(len(tree)):
#     tree[j]+=2*max(N-1-j,j)

# for k in range(len(tree)):
#     print(tree[k])


'''小明用字母 A 对应数字 1，B 对应 2，以此类推，用 Z 对应 26。对于 27
以上的数字，小明用两位或更长位的字符串来对应，例如 AA 对应 27，AB 对
应 28，AZ 对应 52，LQ 对应 329。
请问 2019 对应的字符串是什么？'''

#26进制，先确定位数--3位(容易)

# for a in range(1,26):
#     for b in range(1,26):
#         for c in range(1,26):
#             if(a*(26**2)+b*26+c==2019):
#                 print(a,b,c)
#                 break

#得a=2,b=25,c=17,换算得 "BYQ"


'''给定n个十六进制正整数，输出它们对应的八进制数。
输入格式
　　输入的第一行为一个正整数n （1<=n<=10）。
　　接下来n行，每行一个由0-9、大写字母A~F组成的字符串，表示要转换的十六进制正整数，每个十六进制数长度不超过100000。
　　
输出格式
　　输出n行，每行为输入对应的八进制正整数。
　　
【注意】
　　输入的十六进制数不会有前导0，比如012A。
　　输出的八进制数也不能有前导0。
  
  更多进制转换请参考https://blog.csdn.net/chyuanrufeng/article/details/101478194
  '''
 
# n=int(input())
# li=[]
# if(n>=1 and n<=10):
#     for i in range(n):
#         ori=input()
#         integer=int(ori,16)
#         octnum=oct(integer)
#         li.append(octnum)

# for j in li:
#     print(j[2:])


'''问题描述
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
输入格式
　　输入一行，包含一个正整数n。
输出格式
　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
样例输入
52
样例输出
899998
989989
998899
数据规模和约定
　　1<=n<=54'''


# n=int(input())
# for i in range(10000,1000000): #此处限制数的位数为5或6
#     a=str(i)
#     b=0
#     if a==a[::-1]:#这里的a[::-1]表示把字符串a倒序
#        for j in a:
#            b+=int(j)
#        if b==n:
#            print(a)



'''问题描述
　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=111+555+333。编程求所有满足这种条件的三位十进制数。
输出格式
　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。'''


# for i in range(101,1000):
#     strnum=str(i)
#     a=int(strnum[0])
#     b=int(strnum[1])
#     c=int(strnum[2])
#     if(a**3+b**3+c**3==i):
#         print(i)



'''问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。　　
下面给出了杨辉三角形的前4行：
　　
1　　
1 1　　
1 2 1
1 3 3 1　　
给出n，输出它的前n行。
输入格式
输入包含一个数n。
输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
样例输入
4
样例输出
1
1 1
1 2 1
1 3 3 1 '''

# n=int(input())
# nums=[[0]*n for i in range(n)]#初始化一个n*n的零阵
# for i in range(n):
#     for j in range(n):
#         if j==0:
#             nums[i][j]=1
#         else:
#             nums[i][j]=nums[i-1][j-1]+nums[i-1][j]
#         if nums[i][j]!=0:
#             print(nums[i][j],end=' ')
#     print()     


'''问题描述
利用字母可以组成一些美丽的图形，下面给出了一个例子：

ABCDEFG
BABCDEF
CBABCDE
DCBABCD
EDCBABC

这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。

输入格式
输入一行，包含两个整数n和m，分别表示你要输出的图形的行数的列数。
输出格式
输出n行，每个m个字符，为你的图形。
样例输入
5 7
样例输出
ABCDEFG
BABCDEF
CBABCDE
DCBABCD
EDCBABC '''
    
'''ord()---返回字符对应的asc码
chr()---返回asc码对应的字符'''

# m,n = map(int,input().split())
# for i in range(m):
#     for j in range(n):
#         print(chr(65+abs(i-j)),end = "")
#     print("")


'''问题描述
对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：
00000
00001
00010
00011
00100

请按从小到大的顺序输出这32种01串。
输入格式
本试题没有输入。
输出格式
输出32行，按从小到大的顺序每行一个长度为5的01串。
样例输出
00000
00001
00010
00011 '''

# for i in range(0,32):
#     b=bin(i)[2:]
#     fn='0000'+b
#     print(fn[-5:])



'''问题描述
给定一个年份，判断这一年是不是闰年。
当以下情况之一满足时，这一年是闰年：

年份是4的倍数而不是100的倍数；
年份是400的倍数。
其他的年份都不是闰年。
输入格式
输入包含一个整数y，表示当前的年份。
输出格式
输出一行，如果给定的年份是闰年，则输出yes，否则输出no。 '''


# def is_leapyear():
#     y=int(input())
#     if(y%4==0 and y%100!=0 or y%400==0):
#         print('yes')
#     else:
#         print('no')

# is_leapyear()



# N=int(input())
# li=list(map(int,input().split()))
# layer=int(math.log2(N+1)) #层数
# min=[-1]
# num=0
# for i in range(layer): #遍历每一层
#     add=0
#     for j in range(num,num+2**i): #每一层对应的元素
#         add+=li[j] # 每一层的权值之和
#     num+=2**i
#     min.append(add)   

# print(min.index(max(min)))



'''题目描述
Huffman树在编码中有着广泛的应用。在这里，我们只关心Huffman树的构造过程。
给出一列数{pi}={p0, p1, …, pn-1}，用这列数构造Huffman树的过程如下：

找到{pi}中最小的两个数，设为pa和pb，将pa和pb从{pi}中删除掉，然后将它们的和加入到{pi}中。这个过程的费用记为pa + pb。
重复步骤1，直到{pi}中只剩下一个数。
在上面的操作过程中，把所有的费用相加，就得到了构造Huffman树的总费用。
本题任务：对于给定的一个数列，现在请你求出用该数列构造Huffman树的总费用。
例如，对于数列{pi}={5, 3, 8, 2, 9}，Huffman树的构造过程如下：
找到{5, 3, 8, 2, 9}中最小的两个数，分别是2和3，从{pi}中删除它们并将和5加入，得到{5, 8, 9, 5}，费用为5。
找到{5, 8, 9, 5}中最小的两个数，分别是5和5，从{pi}中删除它们并将和10加入，得到{8, 9, 10}，费用为10。
找到{8, 9, 10}中最小的两个数，分别是8和9，从{pi}中删除它们并将和17加入，得到{10, 17}，费用为17。
找到{10, 17}中最小的两个数，分别是10和17，从{pi}中删除它们并将和27加入，得到{27}，费用为27。
现在，数列中只剩下一个数27，构造过程结束，总费用为5+10+17+27=59。
输入
输入的第一行包含一个正整数n（n< =100）。
接下来是n个正整数，表示p0, p1, …, pn-1，每个数不超过1000。
输出
输出用这些数构造Huffman树的总费用。'''

        
# n=int(input())
# li=list(map(int,input().split()))
# cost=0
# if len(li) == 1:
#     cost=li[0]
# if(n<=100):
    
#     while(len(li)>1):
#         li.sort(reverse=True)
#         a=li.pop()
#         b=li.pop()
#         cost+=a+b
#         li.append(a+b)
#         print(li)

# print(cost)



'''题目描述
给定当前的时间，请用英文的读法将它读出来。
时间用时h和分m表示，在英文的读法中，读一个时间的方法是：
如果m为0，则将时读出来，然后加上“o’clock”，如3:00读作“three o’clock”。
如果m不为0，则将时读出来，然后将分读出来，如5:30读作“five thirty”。
时和分的读法使用的是英文数字的读法，其中0~20读作：
0:zero, 1: one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten, 11:eleven, 
12:twelve, 13:thirteen, 14:fourteen, 15:fifteen, 16:sixteen, 17:seventeen, 18:eighteen, 19:nineteen, 20:twenty。
30读作thirty，40读作forty，50读作fifty。
对于大于20小于60的数字，首先读整十的数，然后再加上个位数。如31首先读30再加1的读法，读作“thirty one”。
按上面的规则21:54读作“twenty one fifty four”，9:07读作“nine seven”，0:15读作“zero fifteen”。
输入
输入包含两个非负整数h和m，表示时间的时和分。非零的数字前没有前导0。h小于24，m小于60。
输出
输出时间时刻的英文。'''

# time={
#       0:'zero', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 
#       12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
#       30:'thirty',40:'forty',50:'fifty','':''
#       }


# h,m=map(int,input().split())
# if(h>20):
#     b=h%20
#     a=h-b
# elif(h<=20):
#     a=''
#     b=h

# if(m>20):
#     if(m<30):
#         d=m%20
#         c=m-d
#     elif(m==30):
#         d=''
#         c=m
#     elif(m<40 and m>30):
#         d=m%30
#         c=m-d
#     elif(m==40):
#         d=''
#         c=m
#     elif(m<50 and m>40):
#         d=m%40
#         c=m-d
#     elif(m==50):
#         d=''
#         c=m
#     elif(m<60 and m>50):
#         d=m%50
#         c=m-d
    
# elif(m<=20):
#     if(m==0):
#         c=''
#         d=' o’clock'
#     else:
#         c=''
#         d=m

# print(time[a]+' '+time[b]+' '+time[c]+' '+time[d])




'''话说这个世界上有各种各样的兔子和乌龟，但是 研究发现，所有的兔子和乌龟都有一个共同的特点——喜欢赛跑。于是世界上各个角落都不断在发生着
乌龟和兔子的比赛，小华对此很感兴趣，于是决定研究不同兔 子和乌龟的赛跑。他发现，兔子虽然跑比乌龟快，但它们有众所周知的毛病——骄傲且懒惰，
于是在与乌龟的比赛中，一旦任一秒结束后兔子发现自己领先t米或以 上，它们就会停下来休息s秒。对于不同的兔子，t，s的数值是不同的，但是所有
的乌龟却是一致——它们不到终点决不停止。然而有些比赛相当漫长，全程观看会耗费大量时间，而小华发现只要在每场比赛开始后记录下兔子和乌龟的
数据——兔子的速度v1（表示每秒兔子能跑v1 米），乌龟的速度v2，以及兔子对应的t，s值，以及赛道的长度l——就能预测出比赛的结果。但是小华很懒，
不想通过手工计算推测出比赛的结果，于是他找 到了你——清华大学计算机系的高才生——请求帮助，请你写一个程序，对于输入的一场比赛的数据v1，v2，
t，s，l，预测该场比赛的结果。
输入
输入只有一行，包含用空格隔开的五个正整数v1，v2，t，s，l，其中(v1,v2< =100;t< =300;s< =10;l< =10000且为v1,v2的公倍数)
输出
输出包含两行，第一行输出比赛结果——一个大写字母“T”或“R”或“D”，分别表示乌龟获胜，兔子获胜，或者两者同时到达终点。
第二行输出一个正整数，表示获胜者（或者双方同时）到达终点所耗费的时间（秒数）。'''


# v1,v2,t,s,l=map(int,input().split())
# dt=0    #兔子的里程
# dg=0    #乌龟的里程
# time=0  #计时器
# while(dt<l and dg<l):
#     if((dt-dg)<t): #兔子未超过乌龟t米
#         dt+=v1
#         dg+=v2
#         time+=1
#     else:
#        for i in range(s):
#            dg+=v2
#            time+=1
#            if(dg==l):
#                break

# if(dt==l and dg<l):
#     print('R')
# if(dg==l and dt<l):
#     print('T')
# if(dt==l and dg==l):
#     print('D')

# print(time)



'''题目描述
有n（2≤n≤20）块芯片，有好有坏，已知1.好芯片比坏芯片多。每个芯片都能用来测试其他芯片。
2.用好芯片测试其他芯片时，能正确给出被测试芯片是好还是坏。而用坏芯片测试其他芯片时，
会随机给出好或是坏的测试结果（即此结果与被测试芯片实际的好坏无关）。
给出所有芯片的测试结果，问哪些芯片是好芯片。
输入
输入数据第一行为一个整数n，表示芯片个数。
第二行到第n+1行为n*n的一张表，每行n个数据。表中的每个数据为0或1，在这n行中的第i行
第j列（1≤i, j≤n）的数据表示用第i块芯片测试第j块芯片时得到的测试结果，1表示好，
0表示坏，i=j时一律为1（并不表示该芯片对本身的测试结果。芯片不能对本 身进行测试）。
输出
按从小到大的顺序输出所有好芯片的编号
样例输入
3
1 0 1
0 1 0
1 0 1
样例输出
1 3 '''


#本题的解法思想就是：
#好芯片比坏芯片数量多，且所有的好芯片对其他好芯片的测试结果都为1。所以，当一个芯片的被测结果为1的数量
# 大于芯片总数的一半（n/2)时，则这个被测芯片是好芯片。

# n=int(input())
# testarray=[]
# ans=[]
# for k in range(n):
#     testarray.append(list(map(int,input().split())))#testarray列表存放芯片的测试结果
# for j in range(n): #每列每列去看
#     num=0
#     for i in range(n):
#         if testarray[i][j]==1:
#             num+=1
#     if num>n/2:
#         print(j+1,end=' ')
    

'''题目描述
FJ在沙盘上写了这样一些字符串：
A1 = “A”     asc 65
A2 = “ABA”
A3 = “ABACABA”
A4 = “ABACABADABACABA”
… …
你能找出其中的规律并写所有的数列AN吗？
输入
仅有一个数：N ≤ 26。
输出
请输出相应的字符串AN，以一个换行符结束。输出中不得含有多余的空格或换行、回车符。 '''
#ord('a')是把a转化为对应的数字，chr('a')是把数字转化为对应的ASCII值

# N=int(input())
# if(N<=26):
#     A1='A'
#     if(N==1):
#         print(A1,end='\n')
#     else:
#         for i in range(1,N):
#             A1=A1+chr(65+i)+A1

#     print(A1,end='\n')



'''最近FJ为他的奶牛们开设了数学分析课，FJ知道若要学好这门课，必须有一个好的三角函数基本功。所以他准备和奶牛们做一个“Sine之舞”的游戏，寓教于乐，提高奶牛们的计算能力。
不妨设
An=sin(1–sin(2+sin(3–sin(4+…sin(n))…)
Sn=(…(A1+n)A2+n-1)A3+…+2)An+1
FJ想让奶牛们计算Sn的值，请你帮助FJ打印出Sn的完整表达式，以方便奶牛们做题。
输入
仅有一个数：N<201。
输出
请输出相应的表达式Sn，以一个换行符结束。输出中不得含有多余的空格或换行、回车符'''

# def An(n,i=1):
#     if i==n:
#         return 'sin('+str(n)+')'
#     else:
#         if i%2==0:
#             s='+'
#         else:
#             s='-'
#         return 'sin('+str(i)+s+An(n,i+1)+')'
# def Sn(m,i=1):
#     if m==1:
#         return An(m)+'+'+str(i)
#     else:
#         return '('+Sn(m-1,i+1)+')'+An(m)+'+'+str(i)
# num=int(input())
# print(Sn(num))


'''Tom教授正在给研究生讲授一门关于基因的课程，有一件事情让他颇为头疼：一条染色体上有成千上万个碱基对，它们从0开始编号，到几百万，几千万，甚至上亿。
比如说，在对学生讲解第1234567009号位置上的碱基时，光看着数字是很难准确的念出来的。
所以，他迫切地需要一个系统，然后当他输入12 3456 7009时，会给出相应的念法：
十二亿三千四百五十六万七千零九
用汉语拼音表示为
shi er yi san qian si bai wu shi liu wan qi qian ling jiu
这样他只需要照着念就可以了。
个音节用一你的任务是帮他设计这样一个系统：给定一个阿拉伯数字串，你帮他按照中文读写的规范转为汉语拼音字串，相邻的两个空格符格开。
注意必须严格按照规范，比如说“10010”读作“yi wan ling yi shi”而不是“yi wan ling shi”，“100000”读作“shi wan”而不是“yi shi wan”，“2000”读作“er qian”而不是“liang qian”。'''

# num=str(input())
# dic={
#      '0':'ling','1':'yi', '2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu'             
#      }



'''问题描述
　　平面上有两个矩形，它们的边平行于直角坐标系的X轴或Y轴。对于每个矩形，我们给出它的一对相对顶点的坐标，请你编程算出两个矩形的交的面积。
输入格式
　　输入仅包含两行，每行描述一个矩形。
　　在每行中，给出矩形的一对相对顶点的坐标，每个点的坐标都用两个绝对值不超过10^7的实数表示。
输出格式
　　输出仅包含一个实数，为交的面积，保留到小数后两位。
样例输入
1 1 3 3
2 2 4 4
样例输出
1.00'''

# while True:
#     try:
#         s1 = list(map(float, input().split()))
#         s2 = list(map(float, input().split()))
#         if s1[0] > s1[2]:
#             s1[0],s1[2] = s1[2],s1[0]
#         if s1[1] > s1[3]:
#             s1[1], s1[3] = s1[3], s1[1]
#         if s2[0] > s2[2]:
#             s2[0],s2[2] = s2[2],s2[0]
#         if s2[1] > s2[3]:
#             s2[1],s2[3] = s2[3],s2[1]
#         temp_x1 = max(s1[0],s2[0])
#         temp_x2 = min(s1[2],s2[2])
#         temp_y1 = max(s1[1],s2[1])
#         temp_y2 = min(s1[3],s2[3])
#         if temp_x2-temp_x1<0 or temp_y2-temp_y1<0: #不相交
#             res = 0
#         else:
#             res = (temp_y2-temp_y1)*(temp_x2-temp_x1)
#         print("{:.2f}".format(res))
#     except:
#         break


'''问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1a2a3…(a1<=a2<=a3…，k也是从小到大的)(具体可看样例)
样例输入
3 10
样例输出
3=3
4=22
5=5
6=23
7=7
8=222
9=33
10=25
提示
　　先筛出所有素数，然后再分解。
数据规模和约定
　　2<=a<=b<=10000 '''

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# a,b=map(int,input().split())
# for num in range(a,b+1):
#     if(is_prime(num)):
#         print('{}={}'.format(num, num))
#     else:
#        li=[]
#        i=2
#        count=num
#        while(True):
#            if(num%i==0):
#                li.append(i)
#                num=num/i
#                if(num==1):
#                    break
#            else:
#                i+=1
#        print(int(count),'=',end='',sep='')    
#        for j in range(len(li)-1):
#            print(li[j],end='')
#        print(li[-1])
       

'''题目描述
给定两个仅由大写字母或小写字母组成的字符串(长度介于1到10之间)，它们之间的关系是以下4中情况之一：
1：两个字符串长度不等。比如 Beijing 和 Hebei
2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing
3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和 BEIjing
4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing
编程判断输入的两个字符串之间的关系属于这四类中的哪一类，给出所属的类的编号。
输入
包括两行，每行都是一个字符串
输出
仅有一个数字，表明这两个字符串的关系编号
样例输入
BEIjing
beiJing
样例输出
3 '''

# str1=str(input())
# str2=str(input())
# if(len(str1)!=len(str2)):
#     print(1)
# else:
#     flag=0
#     for i in range(len(str1)):
#         if(str1[i]==str2[i]):
#             flag+=1
#         elif(abs(ord(str1[i])-ord(str2[i]))==32):
#             flag+=2
#         else:
#             flag+=0
    
#     if(flag==len(str1)):
#         print(2)
#     elif(flag>len(str1)):
#         print(3)
#     else:
#         print(4)





'''题目描述
给定一个以秒为单位的时间t，要求用 “< H> :< M> :< S> ”的格式来表示这个时间。< H> 表示时间，< M> 表示分钟， 而< S> 表示秒，
它们都是整数且没有前导的“0”。例如，若t=0，则应输出是“0:0:0”；若t=3661，则输出“1:1:1”。
输入
输入只有一行，是一个整数t（0< =t< =86399）。
输出
输出只有一行，是以“< H> :< M> :< S> ”的格式所表示的时间，不包括引号。
样例输入
5436
样例输出
1:30:36'''


# time=int(input())
# if(time>=0 and time<=86399):
#     h = int(time/3600)
#     m = int((time%3600)/60)
#     s = int((time%3600)%60)
#     print(str(h)+":"+str(m)+":"+str(s))
    












