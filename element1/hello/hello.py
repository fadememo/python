import keyword
import math
print("hello majoy")
#1 运算符号
    #1.1 算术运算符
print(3+2,end="|")#
print(3-2,end="|")#
print(3*2,end="|")#
print(3/2)#除法 1.5
print(3//2,end="|")#整除1
print(5%2,end="|")#求余1
print(5**2,end="|")#乘方运算
print(math.trunc(5/2))#截取
    #比较运算符
'''
             ==等于 - 比较对象是否相等
            !=不等于 - 比较两个对象是否不相等
            >大于 - 返回x是否大于y
            <小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。
            >=大于等于 - 返回x是否大于等于y。
            <=小于等于 - 返回x是否小于等于y。
'''
    #1.3 赋值运算符
'''
            +=加法赋值运算符
            -=减法赋值运算符
            *=乘法赋值运算符
            /=除法赋值运算符
            %=取模赋值运算符
            **=幂赋值运算符
            //=取整除赋值运算符
'''
    #1.4 逻辑运算符
'''
            逻辑运算符 有 and or not
'''
a=b=1;c=0;d=10
if(a and b):
    print("a和 b 是真心的")   #为真
if(c or d):
    print("谁也不能阻挡")
if(not c):
    print("c 是个骗子")
    # 1.5成员运算符
''''
            in ,not in 判断从属关系
'''
arr1=(1,2,3)
print(1 in arr1)
    # 身份运算符
'''
            is , is not 判断两个标识符是不是引用自一个对象
'''
a="123"
b="123"
c=123
if( a is b): #是同一个对象
    print("ab是一双生")
else:
    print("看这里,不是一起的啦")
print(id(a))
print(id(b))
#2 python保留字
print(keyword.kwlist)
'''
        保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
        ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
# 3注释
#单行
'''多行'''

#4 多行连接    #不可行
'''
majoy = item_1 + \
        item_2 + \
        item_3
print(majoy)
'''

total = [1,2,3,4,
         5,6,7]
print(total)
#print(& total) ???怎么输出内存地址来的? 使用id(var)

# 5 数据类型
'''
            Python3 中有六个标准的数据类型：
            • Number（数字）
            • String（字符串）
            • List（列表）
            • Tuple（元组）
            • Sets（集合）
            Dictionary（字典）
'''

# 5.0 赋值
'''
            • 1,支持多个赋值,支持并行赋值
            • 2、一个变量可以通过赋值指向不同类型的对象。
            • 3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
            • 4、在混合计算时，Python会把整型转换成为浮点数。
'''
a=b=c=d=1
a="anothertype"
test1,test2=2.00,"run away"
print(a+str(b))
print(str(test1)+test2)
    # 5.1 ,isintance() 和 type()
'''
            区别就是:
            • type()不会认为子类是一种父类类型。
            isinstance()会认为子类是一种父类类型。
'''
print(isinstance(3,int))    #True
print(type(3))              #<class 'int'>
    #5.1 number数字
'''
            python中数有四种类型：整数、长整数、浮点数和复数。
            复数可以使用 a+bj 和complex(a,b)表示
'''
a = 3+2j
b = 3-2j
c = 3E2 #3*10^-2
d=complex(3,8)
print("a+b+d=",a+b+d)
print(a*b)
print(c)

    # 5.2,字符串
'''
            Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
            字符串的截取的语法格式如下：变量[头下标:尾下标];索引值以 0 为开始值，-1 为从末尾的开始位置。
            加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。
            Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
'''
s1 = "test1"
print("s1 = ",s1)
s2 = 'test2'
print("s3 = ",s2)
s3 ='''test3
'''
print("s3 = ",s3)
s4 = r"test4\n"
print("s4 = ",s4)
s5 = "test5"
print("s5 = ",s5)
s6 = "test6\n"#转义\
print("s6 = ",s6)
print(s5[0:3],"拼接",s5[0:-5])
print(s5[-5:-3])    #只能从小到大截取
print(s5[0:-2])    #从大到小截取为空
print(s5[3:1])      #从大到小截取为空
print(s5*2)         #复制字符串使用*
    # 5.2.1 字符串的方法
'''
            方法及描述
            capitalize()将字符串的第一个字符转换为大写
            center(width, fillchar)返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
            count(str, beg= 0,end=len(string))返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
            bytes.decode(encoding="utf-8", errors="strict")Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
            encode(encoding='UTF-8',errors='strict')以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
            endswith(suffix, beg=0, end=len(string))检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
            expandtabs(tabsize=8)把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
            find(str, beg=0 end=len(string))检测 str 是否包含在字符串中 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
            index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在字符串中会报一个异常.
            isalnum()如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
            isalpha()如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
            isdigit()如果字符串只包含数字则返回 True 否则返回 False..
            islower()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
            isnumeric()如果字符串中只包含数字字符，则返回 True，否则返回 False
            isspace()如果字符串中只包含空格，则返回 True，否则返回 False.
            istitle()如果字符串是标题化的(见 title())则返回 True，否则返回 False
            isupper()如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
            join(seq)以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
            len(string)返回字符串长度
            ljust(width[, fillchar])返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
            lower()转换字符串中所有大写字符为小写.
            lstrip()截掉字符串左边的空格
            maketrans()创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
            max(str)返回字符串 str 中最大的字母。
            min(str)返回字符串 str 中最小的字母。
            replace(old, new [, max])把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
            rfind(str, beg=0,end=len(string))类似于 find()函数，不过是从右边开始查找.
            rindex( str, beg=0, end=len(string))类似于 index()，不过是从右边开始.
            rjust(width,[, fillchar])返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
            rstrip()删除字符串字符串末尾的空格.
            split(str="", num=string.count(str))num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
            splitlines([keepends])按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
            startswith(str, beg=0,end=len(string))检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
            strip([chars])在字符串上执行 lstrip()和 rstrip()
            swapcase()将字符串中大写转换为小写，小写转换为大写
            title()返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
            translate(table, deletechars="")根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
            upper()转换字符串中的小写字母为大写
            zfill (width)返回长度为 width 的字符串，原字符串右对齐，前面填充0
            isdecimal()检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
s1 = "majoy Never Die 1320 老兵不死"
seq = ("1","2","3","4","5","6")
print(s1.capitalize())
print(s1.center(30,"F"))
print(s1.count("e",1,10))
enstr = s1.encode(encoding="utf-8", errors="strict")
print(enstr)
print(enstr.decode(encoding="utf-8", errors="strict"))
print(s1.expandtabs(4))#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
print(s1.find("e",0,9))
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
print(s1.islower())
print("-".join(seq))#连接序列为字符串
print(s1.ljust(30,"$"))#ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
print(s1.lstrip())
print(s1.maketrans("ae","12"))
print(s1.swapcase())#转换大小写
print(s1.translate("e"))
print(s1.split())
print(((s1+"\n")*5).splitlines())
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)

print("###############################################")
    #5.3 列表
'''
            
            列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
            列表是写在方括号([])之间、用逗号分隔开的元素列表。
            和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
            列表截取的语法格式如下：
            变量[头下标:尾下标],索引值以 0 为开始值，-1 为从末尾的开始位置。
            加号（+）是列表连接运算符，星号（*）是重复操作。
'''

arr1 = [1,2,3,4]
arr2 = [[1,2,3],[2,3]]
arr3 = [1,2,"majoy"]#不同类型元素的列表
print(arr1+arr2)#列表连接
print(arr2 * 2)#列表复制
print(arr3)
        #5.3.1 列表的方法
'''
list.append(obj)在列表末尾添加新的对象
list.count(obj)统计某个元素在列表中出现的次数
list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)将对象插入列表
list.pop(obj=list[-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)移除列表中某个值的第一个匹配项
list.reverse()反向列表中元素
list.sort([func])对原列表进行排序
list.clear()清空列表
list.copy()复制列表
'''
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
list = [1,2,3,4,5]
list.append(7)
print(list)
print(list.count(3))
list.extend(list)#拼接列表
print(list)
print(list.index(3))
list.insert(0,99)
print(list)#在指定索引处插入元素
list.pop(4)#从栈底弹出
print(list)#输入索引
list.remove(2)#从栈底移除
print(list)#输入元素
list.reverse()
print(list)
list.sort()
print(list)
print(list.copy())
print(list.clear())

    #5.4 元组
'''
            元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
            元组中的元素类型也可以不相同
            但它可以包含可变的对象，比如list列表。
            构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
            tup1 = ()    # 空元组
            tup2 = (20,) # 一个元素，需要在元素后添加逗号
            元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

'''
tuple1=(1,2,3,4,"abd",[3,4,5],(6,7))
print(tuple1)
tuple2=()
tuple3=(2,)
print(tuple2+tuple3)
del tuple3
    # 5.4.1 元祖的方法
print(max((1,2,3,4)))
print(len(tuple1))
for i in tuple1:
    print(i)
print("###############################################")
    #5.5 集合
'''
            集合（set）是一个无序不重复元素的序列。 基本功能是进行成员关系测试和删除重复元素。
            可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }。
            集合的运算有 + - & ^
'''
set1={1,2,3,4,"majoy","1"}
set2={2,3,4}
set3=set('23689')
print(set1)#自动进行了某种排序
print(set2)
print(set3)
print(set1|set2)#并集
print(set1-set2)#差集
print(set1&set2)#交集
print(set1^set2)#异或
print("1" in set1)#判断
print("1" not in set1)#判断
    #5.6 字典
'''
        字典（dictionary）是Python中另一个非常有用的内置数据类型。
        列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。        键(key)必须使用不可变类型。
        在同一个字典中，键(key)必须是唯一的。        可以使用键值对生成字典
        键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

'''
dict1={1:"majoy",2:"test","key":"test2"}
dict2={}#
dict3=dict([("key1","value1"),("key2","value2"),("key3","value3")])
dict4={x:x**2 for x in (1,2,3,4,5) }
dict5=dict(Runoob=1, Google=2, Taobao=3)#
dict6=dict(a1=test1, a2=test2, a3="test3") #key作为标识符,必须以字符或者_开头
dict1["key"]="value"
print(dict1.keys())
print(dict1.values())
print(dict3)
print(dict4)
print(dict5)
    # 5.6.1 字典的内置方法
'''
            str(dict)输出字典，以可打印的字符串表示。返回输入的变量类型，如果变量是字典就返回字典类型。
            type(dict)radiansdict.clear()删除字典内所有元素
            radiansdict.copy()返回一个字典的深复制
            radiansdict.fromkeys()创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
            radiansdict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
            key in dict如果键在字典dict里返回true，否则返回false
            radiansdict.items()以列表返回可遍历的(键, 值) 元组数组
            radiansdict.keys()以列表返回一个字典所有的键
            radiansdict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
            radiansdict.update(dict2)把字典dict2的键/值对更新到dict里
            radiansdict.values()以列表返回字典中的所有值
'''
print(str(dict3))
print(type(dict3))
dict5= dict3.copy()
print(dict5)
seq = ("k1","k2","k3")
dict6  = dict3.fromkeys(seq)#使用序列创建字典,值为none
print(dict6)
print(dict3.get("key1"))
dict3.update(dict6)
print(dict3)
print("*****************************************")
        #5.7 数据类型转换
'''
            int(x [,base])	将x转换为一个整数
            float(x)	将x转换到一个浮点数
            complex(real [,imag])	创建一个复数
            str(x)	将对象 x 转换为字符串
            repr(x)	将对象 x 转换为表达式字符串
            eval(str)	用来计算在字符串中的有效Python表达式,并返回一个对象
            tuple(s)	将序列 s 转换为一个元组
            list(s)	将序列 s 转换为一个列表
            set(s)	转换为可变集合
            dict(d)	创建一个字典。d 必须是一个序列 (key,value)元组。
            frozenset(s)	转换为不可变集合
            chr(x)	将一个整数转换为一个字符
            unichr(x)	将一个整数转换为Unicode字符
            ord(x)	将一个字符转换为它的整数值
            hex(x)	将一个整数转换为一个十六进制字符串
            oct(x)	将一个整数转换为一个八进制字符串
'''
print(int("1"))
#print(eval(s2*3))     ???NameError: name 'test2test2test2' is not defined
print(str([1,2,3]))
print(repr([1,2,23,4]))#对象转化为字符串
print(hex(128))#16进制0x80
print(oct(128))#八进制0o200
# 7 等待用户输入
#input("\n\n按下 enter 键后退出。\n\n")

    # 7.1 print 输出 末尾+end
print(s1,end= " ")
print(s2,end= "]]]")
print()
print(s1,s3)
    # 7.2
'''
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
'''

'''
            import 与 from...import
            在 python 用 import 或者 from...import 来导入相应的模块。
            将整个模块(somemodule)导入，格式为： import somemodule
            从某个模块中导入某个函数,格式为： from somemodule import somefunction
            从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
            将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys
print("变量为",sys.argv)
from sys import argv,path
print("变量为",argv,"\n路径为",path)

#打印,不可以留空格
print('╔═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╤═╗')
print('║　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│  ║')
print('║　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　║')
print('║　│春│滟│江│空│江│江│人│不│白│谁│可│玉│此│鸿│昨│江│斜│不│　║')
print('║　│江│滟│流│里│天│畔│生│知│云│家│怜│户│时│雁│夜│水│月│知│　║')
print('║　│潮│随│宛│流│一│何│代│江│一│今│楼│帘│相│长│闲│流│沉│乘│　║')
print('║　│水│波│转│霜│色│人│代│月│片│夜│上│中│望│飞│潭│春│沉│月│　║')
print('║　│连│千│绕│不│无│初│无│待│去│扁│月│卷│不│光│梦│去│藏│几│　║')
print('║春│海│万│芳│觉│纤│见│穷│何│悠│舟│徘│不│相│不│落│欲│海│人│　║')
print('║江│平│里│甸│飞│尘│月│已│人│悠│子│徊│去│闻│度│花│尽│雾│归│　║')
print('║花│，│，│，│，│，│，│，│，│，│，│，│，│，│，│，│，│，│，│　║')
print('║月│海│何│月│汀│皎│江│江│但│青│何│应│捣│愿│鱼│可│江│碣│落│　║')
print('║夜│上│处│照│上│皎│月│月│见│枫│处│照│衣│逐│龙│怜│潭│石│月│　║')
print('║　│明│春│花│白│空│何│年│长│浦│相│离│砧│月│潜│春│落│潇│摇│　║')
print('║　│月│江│林│沙│中│年│年│江│上│思│人│上│华│跃│半│月│湘│情│　║')
print('║　│共│无│皆│看│孤│初│望│送│不│明│妆│拂│流│水│不│复│无│满│　║')
print('║　│潮│月│似│不│月│照│相│流│胜│月│镜│还│照│成│还│西│限│江│　║')
print('║　│生│明│霰│见│轮│人│似│水│愁│楼│台│来│君│文│家│斜│路│树│　║')
print('║　│。│。│。│。│。│？│。│。│。│？│。│。│。│。│。│。│。│。│　║')
print('║　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　║')
print('║　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　│　║')
print('╚═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╧═╝')

# 9,输入 此处缺少一个包
'''
            在Python中，获取键盘输入的数据的方法是采用 raw_input 函数
'''
'''
import 
password = raw_input("请在此输入密码:")
print("您输入的密码是",password)
'''





#12 清理对象
del test1,test2

#13 重要类
    #13.1 数学运算
'''
            abs(x)	返回数字的绝对值，如abs(-10) 返回 10
            ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
            cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
            exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
            fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
            floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
            log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
            log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
            max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
            min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
            modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
            pow(x, y)	x**y 运算后的值。
            round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
            sqrt(x)	返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
            
            随机数函数
            函数	描述
            choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
            randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
            random()	随机生成下一个实数，它在[0,1)范围内。
            seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
            shuffle(lst)	将序列的所有元素随机排序
            uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。            
            三角函数
            acos(x)	返回x的反余弦弧度值。
            asin(x)	返回x的反正弦弧度值。
            atan(x)	返回x的反正切弧度值。
            atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
            cos(x)	返回x的弧度的余弦值。
            hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
            sin(x)	返回的x弧度的正弦值。
            tan(x)	返回x弧度的正切值。
            degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
            radians(x)	将角度转换为弧度
'''
import random
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(abs(-100))
print(math.fabs(-100))
print(math.modf(100.34))#拆分 整数和小数
print(math.fmod(10,4))#取余数
print(math.pow(3,4))#次方
print(math.sqrt(4))#平方根
print(math.radians(12))#radians() 方法将角度转换为弧度。
print(math.degrees(1))#转弧度为角度
print(max(1,2,3,4,5,6,7))
print(round(3.555,3))


print(random.choice(range(100)))#随机取数
print(random.randrange(0,100,1))#指定参数始终和步长 取数
print(random.random())#随机 0,1 之间
random.seed("ok")#替换随机数种子
print(random.random())#
print(range(100))
print(random.shuffle([1,3,2,4]))#输出随机洗牌后的序列
print(random.uniform(4,100))#输出随机实数
print(math.e)
print(math.pi)









