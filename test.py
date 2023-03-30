
# list=[1,2,3,4,5,6,7,8,9,10]
# new=[]
# for i in list:
#     if(i%2 == 0):
#         new.append(i)
# print(new)

# f = open("C:\\Users\\86189\\Desktop\\test.txt", "r",encoding="UTF-8")
# print(f"{f.readlines()}")
# for line in f: #通过循环读取每一行
#     print(f"{line}")
# f.close()  #关闭文件

# with open("C:\\Users\\86189\\Desktop\\test.txt", "r",encoding="UTF-8") as f:
#     for line in f:
#         print(f"{line}")   #执行完自动关闭文件

#读取文件中出现某字符串的次数
# f = open("C:\\Users\\86189\\Desktop\\test.txt", "r", encoding="UTF-8")
# content = f.read()
# f.close()
# num = content.count("ass")
# print(f"出现ass的次数是：{num}")

#文件写入追加
# f = open("C:\\Users\\86189\\Desktop\\test.txt", "a", encoding="UTF-8")#追加
# f.write("\n我们鼠鼠啊，就是这样的捏\n 就是要摆烂的捏") #追加
# f.flush()
# f = open("C:\\Users\\86189\\Desktop\\test.txt", "r", encoding="UTF-8")
# content = f.read()
# print(content)
# f.close()

#异常与捕获异常
# f= None
# try: #尝试
#     f = open("C:\\Users\\86189\\Desktop\\test.txt", "r", encoding="UTF-8")
#     content = f.read()
#     print(f"文件内容如下↓\n{content}")
# except Exception as e:
#     print(f"程序出现异常 ，原因是：{e}")
# finally:
#     if f:    #如果变量是None，f为假，否则为真
#         f.close()


'''自定义模块引用'''
import time

# from mod1 import add
# print(f"sum={add(3,5)}")


#python包
# import my_package.my_mod1
# my_package.my_mod1.info_print()
# or ↓
# from my_package import my_mod1
# my_mod1.info_print()


# d={
#     "性别":"male",
#     "年龄":"18"
# }
#
# def func(a,**kwargs):
#     print(a)
#     print(kwargs)
#
# func(100,**d)

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

'''Python 冒泡排序'''

# def bubbleSort(arr):
#     n = len(arr)
#
#     # 遍历所有数组元素
#     for i in range(n):
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:       #交换位置
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
#
# bubbleSort(arr)
#
# print("排序后的数组:" , arr)
# result = lambda x: x * x
# print(result(5))
#
# numbers = [1, 3, 6]
# newNumbers = tuple(map(lambda x: x , numbers))
# print(newNumbers)



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




