# Python,主讲：汤小洋

## 一、Python简介

### 1. Python是什么？

​	Python是一种面向对象的**解释型**计算机程序设计语言，由荷兰人Guido van Rossum（龟叔）于1989年发明，第一个公开发行版发行于1991年。

​	诞生：1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，即Python（TIOBE编程语言排行榜）

​	作用：开发网站、后台服务、工具脚本、爬虫、数据分析、人工智能等

​	特点：

- 优点：简单（定位：简单、优雅、明确）、代码量少（人生苦短 我用python）、功能强大（大量的第三方库）
- 缺点：运行速度慢、代码不能加密
- 补充：Python是一门解释型语言，不需要编译，类似于PHP，不同于Java、C#等编译型语言

### 2.  安装Python

​	Python是跨平台的，执行Python代码需要解释器

​	版本：2.x、 3.x

​	安装步骤：

- Windows

- Linux

  ```bash
  mkdir python # 创建Python的安装目录

  tar zxf Python-3.6.5.tgz # 解压缩
  cd Pyton-3.6.5
  ./configure --prefix=/home/soft01/python  # 配置，指定安装位置
  make # 编译
  make install # 安装

  cd /home/soft01/python/bin
  ./python3

  # 将python路径添加到PATH变量中
  vi ~/.bashrc
  	export PATH=/home/soft01/python/bin:$PATH
  source ~/.bashrc
  ```

  ​

## 二、第一个Python程序

### 1. 使用Python交互模式

​	执行`python`命令，就进入Python交互模式，提示符`>>>`，输入`exit()`退出交互模式

```python
>>> 3+8
11
>>> print('Hello World')
Hello World
>>> name='tom'
>>> print(name)
tom
>>>exit()
```

### 2. 使用文本编辑器

​	建议使用sublime或notepad++等，不要使用windows自带的记事本（会自动在文件的开头添加特殊字符）

​	步骤：

1. 创建Python脚本文件，以.py结尾

   ```python
   # -*- coding: utf-8 -*-
   # 这是注释，第一个Python程序

   print('Hello World')
   name='唐伯虎'
   print(name)
   ```

   注：如果脚本中有中文，可能会报错，需要在文件的第一行添加一个特殊的注释

2. 运行脚本

   ```bash
   python hello.py
   ```

3. 直接执行脚本

   在Linux和Mac中可以直接执行.py脚本文件，方法：

   - 在文件的第一行添加一个特殊的注释：`#!/usr/bin/env python3`
   - 为文件添加执行权限：`chmod a+x hello.py`
   - 直接执行脚本文件：`./hello.py`

### 3. 使用IDE工具

​	PyCharm，JetBrain公司出口 

​	使用步骤：

1.  创建包

   包中必须存在一个`__init__.py`文件，用于标识这是一个包

2. 创建Python脚本

   ```python
   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-
   __author__ = '汤小洋'

   # 输出，使用print()
   print('hello world')
   name = 'alice'
   print(name)
   ```


### 4. 基本使用

​	输入和输出

- 使用print()
- 使用input()

​       注释：

- 单行注释，以`#`开头
- 多行注释，使用三对单引号或三对双引号

​        编码规范：

- 不要在行尾加分号
- 大小写敏感
- 适应添加空格、空行，使代码布局更优雅、美观、合理
- 使用缩进来表示代码块

## 三、Python基础

### 1. 变量和数据类型

​	变量：

- 定义变量时不需要指定变量的类型，直接为变量赋值即可
- 变量名要符合命名规范

​        数据类型：整型、浮点型、字符串、布尔、空值等

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
   数据类型：整型、浮点型、字符串、布尔、空值等
'''
# 整型int
a = 3454566666666666666
print(a)
print(type(a))

# 浮点型float
b = 12.5
print(b, type(b))

# 字符串str，定义字符串可以使用单引号或双引号（推荐用单引号）
c = 'ccc'
d = "ddd"
print(c, type(c))

print('张三说："今晚吃鸡吗？"')

# 字符串有多行时可以使用三对单引号，表示多行内容
e = '''
welcome 
    to
        itany    
'''
print(e)
print(type(e))

# 布尔bool，取值：True、False
f = True
print(f, type(f))

g = 5 < 3
print(g)

print(5 + False)  # True表示1，False表示0

# 空值 NoneType
h = None
print(h, type(h))
```

### 2. 字符串

​	类型转换

```python
# 将字符串转换数值
a = '25'
b = int(a)
print(type(a), type(b))
c = '12.5'
d = float(c)
print(type(c), type(d))
# 将数值转换为字符串
print('hello ' + str(25))  # 数值类型不能直接和字符中进行拼接，需要进行类型转换
```

​	字符串常用方法

```python
string = '  hello world '
print(string.islower())
print(string.isupper())
print(string.capitalize())
print(string.index('llo'))
print(string)
print(string.strip())  # 类似于java中的trim
print(len(string))  # 调用len()函数获取长度
```

​	切片

```python
name = 'tom cruise'
print(name[0])
print(name[4], name[len(name) - 1], name[-1])
print(name[1:5])  # 获取索引为[1,5)的字符
print(name[:5])  # 表示从头获取
print(name[2:])  # 表示获取到末尾
print(name[1:8:2])  # 索引为[1,8)的字符，每两个取一个
print(name[::2])  # 所有字符，每两个取一个
```

​	格式化

```python
# 格式化字符串，在字符串中指定占位符
# 方式1：使用%运算符，%s表示任意字符，%d表示整数，%f表示浮点数
name = 'tomaaaa'
age = 20
height = 180.5
print('大家好，我叫' + name + '，年龄：' + str(age) + '，身高：' + str(height))
print('大家好，我叫%2.4s，年龄：%d，身高：%.2f' % (name, age, height))  # 2.4s表示字符串长度为2-4位，.2f表示保留两位小数
print('当前时间：%d年-%02d月-%d日' % (2018, 5, 14))  # 指定月份为两位，不足两位则补0

# 方式2：使用format()方法，使用{}表示占位符
print('大家好，我叫{0}，年龄：{1}，身高：{2:.2f}'.format(name, age, height))
print('大家好，我叫{name}，年龄：{age}，身高：{height}'.format(age=age, name=name, height=height))

# 方式3：在字符串前面添加一个f，使用{变量名}来嵌入变量
print(f'大家好，我叫{name}，年龄：{age}，身高：{height}')
```

### 3. 运算符

​	算术运算符、比较运算符、赋值运算符、逻辑运算符、位运算符、条件运算符、成员运算符、身份运算符

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

'''
Python中支持的运算符：
1.算术运算符
    + - * / % // **
    不支持自增++和自减--
2.比较运算符
    > < >= <= == !=或<> 
3.赋值运算符
    = += -= *= /+ %= **=
4.逻辑运算符
    and  or  not
5.条件运算符，也称三目运算符
    语法：条件为真时的结果 if 条件 else 条件为假时的结果  
6.位运算符
    与& 或| 非~  异或^ 左移<<  右移>>
7.成员运算符
    in 
    not in
8.身份运算符
    is 
    is not
    
'''

# 1.算术运算符
print(3 + 5)
print(3 * 5)
print(30 * '-')  # 乘法可以用于字符串
print(5 % 3)
print(5 / 3)  # 除法，有小数
print(5 // 3)  # 除法，取整
print(2 ** 3)  # 幂
print(pow(2, 3))
i = 5
i = i + 1
print(i)
print('*' * 80)

# 2.比较运算符
j = 5
print(j > 2)
print(10 > j > 1)  # 支持此写法
print('abc' > 'acd')  # 可以用于字符串的比较，比较的是字符串的Unicode编码

# 3.赋值运算符
a = 10
a += 5  # 等价于a= a+5
print(a)

# 4.逻辑运算符
print(True and False)
print(5 > 2 or 4 < 1)
print(not 5 > 2)

x = 0  # 0 表示False，非0表示True
y = 8
print(x and y)  # 如果ｘ为True，则返回y；否则返回x
print(x or y)  # 如果x为True，则返回x；否则返回y
print(not x)  # 如果x为True，则返回False，否则返回True

# 5.条件运算符，也称三目运算符
print('aaa' if 5 < 2 else 'bbb')

# 6.位运算符
a = 5  # 00000101
b = 8  # 00001000
print(a & b)  # 两位都是1才为1，否则为0
print(a | b)  # 只要有一位为1，则为1，否则为0
print(~a)  # 如果为1，则为0，如果为0，则为1
print(a ^ b)  # 如果两位相同，则为0，不同为1
print(b >> 2)  # 二进制的所有位都向右移2位

# 7.成员运算符
c = [3, 5, 12, 15, 7, 2]
d = 5
print(d not in c)

# 8.身份运算符
m = [1, 3, 5, 7]
n = [1, 3, 5, 7]
x = n
print(m is n)
print(x is n)

'''
    is 和 == 的区别
    is 判断两个变量是否引用同一个对象
    == 判断两个变量的值是否相等
'''
print(m == n)
```



### 4. 列表和元组

​	列表list是一种有序的集合，用来存储多个值，可以向列表中添加或删除元素

​	元组tuple与list很类似，也是用来存储多个值，但tuple中的元素只能在定义时初始化，初始化后就无法再修改

​	总结：列表list和元组tuple都是Python内置的一种集合，一个可变的，一个是不可变的

```python
# ---列表list
# 定义列表，使用[]
names = ['tom', 'jack', 'alice', 'mike']
print(names)
print(type(names))

# 获取/设置元素
print(names[1], names[:3])
names[0] = 'lucy'
print(names)

# 追加元素
names.append('zhangsan')

# 在指定位置插入元素
names.insert(1, 'lisi')

# 删除元素
names.remove('jack')

# 弹出元素
print(names.pop(0))

# 获取元素个数
print(len(names))

# 可以存储不同类型的数据
names.append(25)  # 不建议
names.append(True)

print(names)
print('-' * 80)

# ------元组tuple
# 定义元组，使用()
nums = (3, 8, 13, 25, 38, 250)
print(nums)
print(type(nums))

print(nums[2], nums[-1])
print(nums[1:3])

# 解构赋值
# a = nums[0]
# b = nums[1]
# c = nums[2]
# d = nums[3]
# e = nums[4]
# f = nums[5]
a, b, c, d, e, f = nums
print(a, b, c, d, e, f)
```

### 5. 条件判断

​	根据条件进行判断，从而执行不同的操作

​	使用`if...elif...else`语句

### 6. 循环

​	重复性的执行某个操作，称为循环

​	两种：

- while循环
- for...in循环

```python
# ----while循环
# 计算1到100的和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# ----for...in循环
names = ['tom', 'jack', 'alice', 'mike']
for name in names:
    print(name, end=',')
print()

# 使用range()函数生成一个序列
for i in range(1, 100, 2):  # 生成一个[1,100)的整数序列，步长为2
    print(i, end=',')
print()

# 计算1到100的和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
```

​	break和continue关键字

### 7. 字典和集合

​	dict全称dictionary，使用键-值（key-value）存储数据，在其他语言中一般称为map

​	set是无序的，不允许重复	

```python
# ----字典
# 定义dict，使用大括号{}，与js中的json很类似
scores = {'tom': 98, 'jack': 100, 'alice': 60}
print(scores)
print(type(scores))

# 获取
print(scores['jack'])
print(scores.get('alice'))

# 添加/设置
scores['lucy'] = 89
scores['tom'] = 100

# 弹出（删除）
print(scores.pop('tom'))

# 判断是否存在指定的key
print('alice' in scores)

print(scores)

# 遍历
print(scores.keys())
print(scores.values())
print(scores.items())

for k in scores.keys():
    print(k, scores[k])
print('-' * 80)

for v in scores.values():
    print(v)
print('-' * 80)

for k, v in scores.items():
    print(k, v)
print('-' * 80)

# -----set集合
# 定义set，使用大括号{}
# s = {3, 12, 5, 7, 34, 12, 3}
nums = [4, 23, 1, 23, 4, 23]
s = set(nums)  # 调用set()函数将list转换为set，去除重复值
print(s)
print(type(s))

# 添加
s.add(666)
s.add(1)

# 删除
s.remove(1)

print(s)

# 遍历
for i in s:
    print(i)
```

## 四、函数

​	函数是实现特定功能的代码段的封装，在需要时可以多次调用函数来实现该功能

### 1. 内置函数

​	Python内置了许多非常有用的函数，可以直接调用

### 2. 自定义函数

​	语法：

```python
def 函数名(形参1,形参2,...):
    函数体
```

​	注意：

- 函数名可以包含数字、字母、下划线，但不能以数字开头
- 如果函数有返回值，使用return关键字
- 定义函数后函数中的代码并不会执行，需要调用函数才会执行

````python
# 定义函数，使用def
def calc(num1, num2):  # 必选参数，也称为位置参数，不能省略
    res = num1 + num2
    return res


# print(calc(3, 5))  # 调用函数


# 参数类型检查
def my_abs(x):
    # 可以为函数添加文档注释，也称为文档字符串doc string
    """
    计算绝对值
    :param x: 参数
    :return: 返回x的绝对值
    """
    # 对参数类型进行检查
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不正确，只能为数值类型')  # 抛出异常

    if x >= 0:
        return x
    else:
        return -x


# print(my_abs('aaa'))

# print(help(my_abs))


# 默认参数，即有默认值的参数
def my_pow(x, y=2):
    if y == 0:
        return 1
    res = x
    for i in range(y - 1):
        res *= x
    return res


# print(my_pow(5))


# 可变参数，使用*号，表示参数个数是可变的
def my_sum(x, *y):
    print(x)
    print(y)  # 接收到的实际上是一个tuple


# my_sum(3, 5, 8, 12, 4)

# 不建议下面的这种写法，建议将必选参数放在最前面
def my_sum2(*y, x):
    print(y)
    print(x)


# my_sum2(12, 4, 2, 7, x=9)  # 必选参数在后面时需要指定参数名

# 对于可变参数，可以直接传入list或tuple，只需要在参数前添加一个*
nums = [12, 4, 2, 64, 23, 9]


# my_sum(4, nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
# my_sum(4, *nums)


# 关键字参数，使用**，也表示参数个数是可变的，但传递的是带名称的参数
def f1(x, **y):
    print(x)
    print(y)  # 接收到的实际上一个dict


# f1(3, a=5, b=9, c=18)

# 对于关键字参数，可以直接传入一个dict，只需要在参数前添加**
user = {'id': 1001, 'name': 'tom', 'age': 18}


# f1(4, id=user['id'], name=user['name'], age=user['age'])
# f1(4, **user)


# 命名关键字参数，限制关键字参数的名字，使用*分隔，*号后面的参数表示命名关键字参数
def f2(x, *, name, age):
    print(x)
    print(name)
    print(age)


# f2(4, name='alice', age=20)


# 接收任意参数
def f3(*args, **kwargs):
    print(args)
    print(kwargs)


f3(1, 43, 'aaa', name='alice', age=20)
````

```python
# 空函数，表示以后再实现
def empty():
    pass  # 使用pass


# 函数的返回值，返回多个值
def f1():
    name = 'tom'
    age = 20
    sex = 'male'
    return name, age, sex


# print(f1())  # 返回值实际上是一个tuple
a, b, c = f1()


# print(a, b, c)


# 函数的返回值，返回一个函数，即将函数作为返回值
def f2(x):
    print(111)
    z = 6

    def f3(y):
        print(x * y + z)  # 内部函数使用了外部函数的参数或局部变量，称为闭包

    return f3


# fn = f2(3)
# fn(5)


# 递归函数：一个函数在内部调用自身，这个函数就是递归函数
# 计算x的y次方，如计算2的5次方
def calc(x, y):
    # 常规方式
    # if y == 0:
    #     return 1
    # i = 1
    # res = x
    # while i < y:
    #     res *= x
    #     i += 1
    # return res

    # 递归方式
    # 2*2*2*2*2=2*(2*2*2*2)=2*(2*(2*2*2))=
    if y == 0:
        return 1
    else:
        return x * calc(x, y - 1)  # 不停的调用自己，递归太深可能会抛出栈溢出异常

print(calc(2, 99999999999999))
```

### 3. 变量作用域和命名空间

```python
'''
变量作用域scope：指的是变量生效的区域

两种作用域：
1.全局作用域
    函数以外的区域都是全局作用域
    在全局作用域中定义的变量，都是全局变量
2.函数作用域，也称为局部作用域
    函数内的区域，每调用一次函数就会创建一个新的函数作用域
    在函数作用域中定义的变量，都是局部变量
    
变量的查找顺序：
    先在当前作用域中查找，如果没有则向上一级作用域中查找，直到查找全局作用域，如果还是没有，则报错
'''

a = 5  # 全局变量

if True:
    c = 5  # 全局变量，在Python中没有块级作用域


def fn():
    b = 8  # 局部变量
    print('函数内部：a=', a)
    print('函数内部：b=', b)
    print('函数内部：c=', c)


fn()

print('函数外部：a=', a)
# print('函数外部：b=', b)
print('函数外部：c=', c)

x = 1


def f1():
    x = 2

    def f2():
        x = 3
        print(x)


print('-' * 80)


# global关键字
def fn2():
    # a = 10  # 在函数中为变量赋值时，默认都是为局部变量赋值
    # 如果希望在函数中修改全局变量，要使用global关键字来声明变量
    global a
    a = 10

    print('函数内部：a=', a)


fn2()

print('函数外部：a=', a)
print('*' * 80)

'''
命名空间namespace：指的是变量存储的位置，每一个变量都要存储在指定的命名空间中

每个作用域都有一个对应的命名空间
全局命名空间，用来存储全局变量；函数命名空间，用来存储函数中的变量
命名空间实际上就是一个字典dict，是一个专门用来存储变量的字典
'''

# locals() 获取当前作用域的命名空间
scope = locals()  # 在全局作用域中调用locals()，获取的就是全局命名空间
print(scope)
print(type(scope))

# 通过scope操作命名空间中的变量（不建议）
print(scope['a'])
scope['c'] = 666
scope['z'] = 'tom'
print(scope['c'])
print(scope['z'])
# print(z)
print('*' * 80)


def fn3():
    a = 888
    scope = locals()  # 在函数中调用locals()，获取到的是函数命名空间
    scope['b'] = 222
    print(scope)
    print(scope['b'])

    # globals() 可以在任意位置获取全局命名空间
    global_scope = globals()
    print(global_scope)
    print(global_scope['a'])


fn3()
```

### 4. 高级特性

​	迭代和列表生成式

```python
# 导入模块
import collections

'''
迭代：也称为遍历，循环获取每一个元素
'''

for i in ['tom', 'jack', 'alice']:
    print(i, end=' ')
print()

for i in ('tom', 'jack', 'alice'):
    print(i, end=' ')
print()

for i in {'name': 'tom', 'age': 18, 'sex': 'male'}.keys():
    print(i, end=' ')
print()

for k, v in {'name': 'tom', 'age': 18, 'sex': 'male'}.items():
    print(k, v)

for i in 'hello':
    print(i)

# 判断对象是否是可迭代的
print(isinstance('hello', collections.Iterable))

# 获取索引和值
# 方式1：自己获取索引
names = ['tom', 'jack', 'alice']
for i in range(len(names)):
    print(i, names[i])

# 方式2：使用enumerate()函数，转换为索引-元素对
print(enumerate(names))
print(isinstance(enumerate(names), collections.Iterable))
for k, v in enumerate(names):
    print(k, v)

print('-' * 80)

'''
列表生成式：用来创建list的生成式
'''
# 生成[0,99]的list
# nums = range(0, 100)
nums = list(range(0, 100))  # 转换为list
# print(nums, type(nums))

# print(isinstance(range(0, 100), collections.Iterable))

# for i in range(0, 100):
#     print(i)

# 生成一个包含[1,100]之间所有3的倍数的list
# 方式1
# lst = []
# for i in range(1, 101):
#     if i % 3 == 0:
#         lst.append(i)

# 方式2
lst = [i for i in range(1, 101) if i % 3 == 0]  # 等价于a = list(range(1, 101))
print(lst)
```

​	迭代器和生成器

```python
'''
迭代器iterator：用来访问集合元素的一种方式，可以记住迭代的位置
'''

nums = [3, 8, 12, 54, 2, 7]
it = iter(nums)  # 调用iter()函数创建迭代器
print(type(it))

print(next(it))  # 调用next()函数获取迭代器的下一个元素
print(next(it))  # 只能往前不能后退

# 使用for...in循环遍历迭代器
for i in it:
    print(i)

'''
生成器generator：在循环过程中依次计算获取值的对象（节省空间、效率高）
创建生成器的方式：
    方式1：把一个列表生成式的[]改成()
    方式2：在函数中使用yield关键字，此时该函数就变成一个生成器函数
'''
# 方式1：把一个列表生成式的[]改成()
generator = (i for i in range(1, 100))
print(type(generator))  # generator类型

# 获取生成器的下一个值
print(next(generator))  # 获取时才生成值，类似于Oracle中sequence
print(next(generator))
print(next(generator))

# 使用for...in循环遍历生成器
for i in generator:
    print(i)

print('-' * 80)


# 方式2：在函数中使用yield关键字，此时该函数就变成一个生成器函数
def gen():
    print('one')
    yield 13
    print('two')
    yield 8
    print('three')
    yield 25
    print('four')
    yield 38


# 生成器函数与普通函数的执行流程不一样：
# 普通函数是顺序执行，执行到最后一行或遇到return时结束
# 生成器函数是在每次调用next()时执行，遇到yield语句就返回，下一次调用next()时会从上次返回的yield语句处继续执行
g = gen()  # generator类型
print(type(g))
print(next(g))
print(next(g))

# 使用for...in循环遍历生成器
for i in g:
    print(i)
```

​	高阶函数

```python
'''
高阶函数：一个函数接收另一个函数作为参数，这种函数称为高阶函数
'''

nums = [12, -4, 3, -23, 65, 1, -234, 22]


# 定义一个函数，用来检查数字是否大于5
def f1(x):
    if x > 5:
        return True
    return False


# 自定义高阶函数，用来过滤列表中的元素
def fn(fun, lst):
    """
    将列表中所有符合条件的元素筛选出来，返回一个新列表
    :param fun: 条件函数
    :param lst: 要进行筛选的列表
    :return: 返回新列表
    """
    new_list = []
    for i in lst:
        if fun(i):
            new_list.append(i)
    return new_list


nums1 = fn(f1, nums)
print(nums1)


def f2(x):
    return x % 2 == 0


print(fn(f2, nums))

# 内置高阶函数 filter()，用于过滤序列
nums2 = filter(f1, nums)
print(list(nums2))


# 内置高阶函数 map()，用于处理序列
def f3(x):
    return x * x


nums3 = map(f3, nums)
print(list(nums3))


# 内置高阶函数 sorted()，用于排序
print(sorted(nums))
print(sorted(nums,key=abs))
```

​	匿名函数和装饰器

```python

'''
匿名函数：没有名字的函数，使用lambda关键字
'''

nums = [12, 4, 32, 5, 23, 7]

# def fn(x):
#     return x * 2 + 1


nums_new = list(map(lambda x: x * 2 + 1, nums))
print(nums_new)

# 将匿名函数赋给变量（不建议）
a = lambda x: x + 1
print(a(2))

print('-' * 80)

'''
装饰器：在代码运行期间动态增加功能，称为装饰器Decoration，类似于AOP
'''


# 定义一个装饰器，为函数添加打印日志的功能
def log(fn):
    def wrapper(*args, **kwargs):
        print('开始执行%s()函数。。。' % fn.__name__)
        res = fn(*args, **kwargs)
        print('执行%s()函数结束。。。' % fn.__name__)
        return res

    return wrapper  # 返回装饰函数


@log
def even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)


@log
def calc(num1, num2):
    res = num1 + num2
    return res


even([12, 34, 2, 5, 34, 21])

print(calc(3, 5))
```

## 五、面向对象

### 1. 定义类

​	语法：

```python
class 类名：
	类中成员
```

​	类中的成员：实例属性、实例方法、类属性、类方法、静态方法等

```python
# 定义一个类，使用class关键字
class Student:
    # pass

    # 类属性：直接在类中定义的属性，可以通过类或实例对象来访问
    hobby = '吃饭'

    # 实例方法：将self作为第一个参数的方法
    def say_hi(self):  # self表示当前类的实例，类似于java中的this
        print('Hi:' + self.name)

    def say_hello(self, username='无名氏'):
        print('Hello:' + username)

    # 类方法：使用@classmethod修饰的方法，将cls作为第一个参数
    @classmethod
    def show(cls, msg):  # cls表示当前类
        print(msg, cls.hobby)

    # 静态方法：使用@staticmethod修饰的方法，没有任何必选参数，不需要将cls作为第一个参数
    @staticmethod
    def show2(msg):
        print(msg, Student.hobby)


# 创建类的对象
stu1 = Student()  # 创建Student类的一个实例
stu2 = Student()
print(stu1, type(stu1))
print(stu2, type(stu2))

a = 3
print(a, type(a))
b = int(5)  # 创建int类的一个实例
c = str('hello')  # 创建str类的一个实例
print(b, type(b))

# 为对象绑定属性
stu1.name = 'tom'  # 实例属性，通过实例对象添加的属性
stu1.age = 20
stu2.name = 'alice'
stu2.sex = 'female'
stu2.height = 180.5
print(stu1.name, stu1.age)
print(stu2.name, stu2.sex, stu2.height)

# 访问实例方法
stu1.say_hi()  # 调用方法时无需传递self，由解析器调用时将对象作为self自动传入
stu2.say_hi()
stu1.say_hello('张三')
stu2.say_hello()

# 访问类属性
print(Student.hobby)
stu1.hobby = '睡觉'  # 为stu1添加了一个实例属性，并不会改变类属性hobby的值
print(stu1.hobby)
print(stu2.hobby)  # 如果当前实例没有hobby属性，则会向上查找类属性hobby

# 访问类方法
Student.show('hello')  # 调用方法时无需传递cls
stu1.show('Hello')
Student.show2('您好')
stu2.show2('你好')
```

### 2. 构造方法

​	`__init__()` 构造方法，在创建对象时会自动调用，可以用来初始化对象的属性

```python
class Student:

    # 构造方法（函数），不支持重载
    def __init__(self, name, age):
        print('创建对象，执行构造方法。。。')
        self.name = name
        self.age = age

    # 实例方法
    def show(self):
        print('姓名：%s，年龄：%d' % (self.name, self.age))


stu1 = Student('tom', 18)
print(stu1.name, stu1.age)
stu1.show()
```

### 3. 封装、继承、多态

​	封装：隐藏对象中一些不希望被外部所访问到的属性，保证数据的安全

```python
class Student:
    # 定义私有属性
    __age = 18  # 以两个下划线开头，表示对象的隐藏属性，只能在类内部访问

    # 提供getter/setter方法
    def get_age(self):
        return self.__age

    def set_age(self, age):
        # 判断数据是否有效
        if 0 < age < 100:
            self.__age = age
        else:
            self.__age = 18


stu1 = Student()
# print(stu1.__age)  # 在类外部无法访问私有属性
stu1.set_age(28)
print(stu1.get_age())

# 其实Python会把私有属性转为 _类名__属性名（强烈不建议）
print(stu1._Student__age)
```

​	继承：使一个类能够获取到其他类中的属性和方法

```python
# 定义一个Person类，父类（超类、基类）
class Person(object):  # 如果省略了父类，则默认父类为object
    def __init__(self, name):
        self.name = name

    def run(self):
        print('person:' + self.name + '正在奔跑。。。')


# 定义一个Student类，子类
class Student(Person):  # 继承自Person
    def __init__(self, name, email):
        # 调用父类的构造方法
        # Person.__init__(name)  # 方式1：直接指定父类的构造方法
        super().__init__(name)  # 方式2：使用super，推荐
        self.email = email

    # 定义子类特有的方法
    def study(self):
        print('student:' + self.name + '正在学习。。。')

    def show(self):
        print('姓名：%s，邮箱：%s' % (self.name, self.email))

    # 重写父类的方法
    def run(self):
        # super().run()  # 调用父类的方法
        print('student:' + self.name + '正在奔跑。。。。')


stu = Student('tom', 'tom@sina.com')
stu.run()  # 调用子类重写后的方法
stu.study()
stu.show()

# 判断一个对象是否是指定类的实例，即判断对象的类型
print(isinstance(stu, Student))
print(isinstance(stu, Person))

# 判断一个类是否是指定类的子类
print(issubclass(Student, Person))
print(issubclass(Student, object))


# object类是所有类的根类，默认所有类都继承自object
print(stu.__doc__)
print(stu.__dict__)
```

​	多继承

```python
class A:
    def a(self):
        print('a')


class B:
    def b(self):
        print('b')


class C(A, B):  # 继承多个父类，以逗号隔开
    def c(self):
        print('c')


c = C()
c.a()
c.b()
c.c()

# 类的特殊属性 __bases__ 可以用来获取当前类的所有父类
print(C.__bases__)
```

​	多态：多种形态

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('动物在叫。。。。')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def cry(self):
        print('狗在叫。。。。汪汪汪')


class Cat(Animal):
    def __init__(self, name, sex):
        super().__init__(name)
        self.sex = sex

    def cry(self):
        print('猫在叫。。。喵喵喵')


# 一个对象可以以不同的形式去呈现，就是多态
def play(animal):
    print(animal.name)
    animal.cry()


dog = Dog('旺财', 2)
cat = Cat('猫咪', '公')
play(dog)
play(cat)
```

### 4. 魔术方法

​	在类中可以定义一些特殊的方法，称为魔术方法

​	特点：

- 都是以双下划线开头，以双下划线结尾
- 不需要手动调用，在特定时机会自动执行

```python
# 定义一个类
class Person(object):

    def __init__(self, name, age):
        print('__init__')
        self.name = name
        self.age = age

    # 将对象转换为字符串时调用，类似于java中的toString()
    def __str__(self):
        return 'Person [name=%s, age=%d]' % (self.name, self.age)

    # 在对象使用len()函数时调用
    def __len__(self):
        return len(self.name)

    # 在对象使用repr()函数时调用
    def __repr__(self):
        return 'hello person'

    # 将对象转换为bool类型时调用
    def __bool__(self):
        return self.age > 18

    # 在对象进行大于比较时调用
    def __gt__(self, other):  # self表示当前对象，other表示要比较的对象
        return self.age > other.age


p1 = Person('唐伯虎', 20)
p2 = Person('秋香', 18)

print(p1)

print(len(p1))

print(repr(p1))

print(bool(p1))

if p1:
    print(p1.name, '已成年')
else:
    print(p1.name, '未成年')

print(p1 > p2)
```

## 六、模块

### 1. 简介

​	模块化是指将一个程序分解为一个个的模块module，通过组合模块来搭建出一个完整的程序

​	优点：便于团队开发、方便维护、代码复用

​	在Python中一个.py文件就是一个模块，创建模块实际上就是创建一个.py文件，可以被其他模块导入并使用

​	注意：

- 自定义模块时要注意命名规范，使用小写，不要使用中文、特殊字符等
- 不要与内置模块冲突

### 2. 使用模块

​	导入模块的两种方式：

- 方式1：import 包名.模块名 [ as 别名] 

- 方式2：from 包名 import 模块名

  ​              from 包名.模块名 import 变量|函数|类

​        导入模块的代码可以放在任意位置，但一般都放在程序的开头

```python
# 方式1
# import py04_模块.mymodule
# print(py04_模块.mymodule.a)  # 调用模块中的变量
# print(py04_模块.mymodule.plus(3, 5))

# import py04_模块.mymodule as m
# print(m.plus(3, 5))

# 方式2
# from py04_模块 import mymodule
# print(mymodule.b)
# print(mymodule.minus(8, 2))

from py04_模块.mymodule import b, plus, Calculator

# from py04_模块.mymodule import *  # 不建议

# print(b)
# print(plus(2, 5))
# print(Calculator.sum(3, 12, 5))
```

```python
'''
__name__属性是模块的内置属性，每个模块中都有该属性
当该.py文件是主执行文件，直接被执行时，其值为__main__
当该.py文件是被调用，导入执行时，其值为模块名
'''
# print(__name__)

# 程序入门，类似于Java中的main()方法，只在当直接调用该文件时才会执行，用来执行测试
if __name__ == '__main__':
    print(Calculator.sum(1, 2, 3))
```

### 3. Python标准库

​	Python提供了一个强大的标准库，内置了许多非常有用的模块，可以直接使用（标准库是随Python一起安装）

​	常用的内置模块：

- sys：获取Python解析的信息
- os：对操作系统进行访问，主要是对目录或文件进行操作
- math：数学运算
- random：生成随机数
- datetime：处理日期和时间，提供了多个类
- time：处理时间

```python
import sys
import os
import math
import random
from datetime import datetime, timedelta
import time

print(sys.version)  # Python版本
print(sys.platform)  # 系统平台
print(sys.argv)  # 命令行参数
print(sys.path)  # 模块搜索路径，包含了Python解析器查找模块的搜索路径
print(sys.modules)  # 显示当前程序中引入的所有模块
print(sys.getdefaultencoding())  # 默认字符集
# sys.exit('程序退出') # 退出解析器
print('---------------------------------')

print(os.name)  # 操作系统的类型
print(os.environ['path'])  # 系统的环境变量
print(os.getcwd())  # 当前的目录
print(os.listdir('d:/'))  # 列出指定目录中的内容
# os.system('ping www.baidu.com')  # 执行系统命令
print(os.path.exists('d:/soft'))  # 判断路径是否存在
print('---------------------------------')

print(math.pi)
print(math.ceil(3.4))
print(math.floor(3.4))
print(math.pow(2, 3))
print(math.trunc(2.6))  # 截尾取整
print(round(2.6))
print(round(3.1415925, 3))  # 四舍五入，保留三位小数
print('---------------------------------')

print(random.random())  # 返回[0,1)之间的随机浮点数
print(random.randint(1, 101))  # 返回[1,100]之间的随机整数
print(random.sample([1, 21, 54, 23, 6, 2], 2))  # 从数组中返回随机两个元素
print('---------------------------------')

print(datetime.now(), type(datetime.now()))  # 返回当前时间
print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))  # 将datetime转换为指定格式的str
print(datetime.strftime(datetime.now(), '%Y{0}%m{1}%d{2} %H:%M:%S').format('年', '月', '日'))
print(datetime.strptime('2018-2-14', '%Y-%m-%d'))  # 将str转换为datetime
print('明天：', datetime.now() + timedelta(days=1))  # timedelta表示两个时间之间的时间差，可以用来进行日间的加减操作
print('前一秒：', datetime.now() - timedelta(seconds=1))
print('---------------------------------')

print(time.time())  # 返回当前时间的时间戳
print(int(time.time()))  # 秒级时间戳
print(int(time.time() * 1000))  # 毫秒时间戳
time.sleep(5)  # 休眠5秒
print(1111)
```

### 4. 第三方模块

​	Python社区提供了大量的第三方模块，使用方式与标准库类似

​	安装第三方模块：

- 使用包管理工具pip（随Python一起安装的）

  ```python
  pip install 模块名
  ```

- 使用PyCharm来安装

  Settings——>Project——>Project Interpreter

  报错：`AttributeError: module 'pip' has no attribute 'main'`

  解决：找到PyCharm安装目录下的helpers/packaging_tool.py文件，替换其中的do_install和do_uninstall函数

  注：官方仓库比较慢，可以使用豆瓣提供的镜像仓库 https://pypi.douban.com/simple/



​	pyecharts是一个用于Echarts图表的类库，便于在Python中根据数据生成可视化的图表

​	Echarts是百度开源的一个数据可视化JS库，主要用来进行数据可视化。

​	参考：http://pyecharts.org

​	安装pyecharts库

​	新版本的pyecharts默认不带地图文件，如果需要使用地图，需要自行安装地图文件包

## 七、异常处理和IO操作

### 1. 异常处理

​	语法：

```python
try:
    可能出现异常的代码
except:
    出现异常后要执行的操作
else:
    不出现异常时执行的操作
finally:
    无论是否出现异常都必须要执行的操作
```

```python
try:
    print('try...')
    a = 5 / int('abc')
# except:  # 捕获所有异常
# except ZeroDivisionError as e:  # 捕获ZeroDivisionError异常，获取到异常对象
except (ZeroDivisionError, ValueError, Exception) as e:  # 捕获多种异常
    print('出现异常啦', e)
else:
    print('没有异常时执行')
finally:
    print('finally...')


# 自定义异常，继承自Exception(Exception类是所有异常类的父类)
class UsernameExistsException(Exception):
    pass


def fn(username):
    if username == 'admin' or username == 'tom':
        raise UsernameExistsException('用户名已存在')  # 使用raise抛出异常
    else:
        print('ok')


fn(input('请输入用户名：'))
```

### 2. IO操作

​	文件操作

```python
'''
读写模式：
    r  读模式
    w  写模式（覆盖）
    a  追加模式
    r+ 读写模式
    b  二进制模式
'''

# ----读取文件
try:
    f = open('itany.txt', mode='r', encoding='utf-8')  # 打开一个文件，返回一个对象，这个对象就代表着当前打开的文件
    print(f.read())  # 一次性读取所有内容
except FileNotFoundError as e:
    print('文件找不到：', e)
finally:
    if f:
        f.close()  # 文件操作后一定要关闭

print('-' * 80)

# 简写，使用with...as语句，会自动调用close()
with open('itany.txt', mode='r', encoding='utf-8') as f:
    # print(f.read())
    # print(f.read(3))  # 每次读取3个字符
    # print(f.read(3))
    # print(f.readline().strip())  # 每次读取一行
    # print(f.readline())
    lines = f.readlines()  # 一次性读取所有行，返回list
    # print(lines)
    for line in lines:
        print(line.strip())

print('-' * 80)

# ----写文件
with open('itany.txt', mode='a', encoding='utf-8') as f:
    f.write('xxx\n')
    f.write('yyy')

print('-' * 80)

# ----读写二进制文件
with open('baidu.png', mode='rb') as f:
    with open('itany.png', mode='wb') as out:
        out.write(f.read())
        print('拷贝成功')
```

​	文件操作模块

```python
import os
import shutil

# ----操作文件和目录
print(os.path.exists('itany.txt'))  # 判断是否存在
print(os.path.abspath('itany.txt'))  # 文件的绝对路径
print(os.path.isfile('itany.txt'))  # 判断是否为文件
print(os.path.isdir('itany.txt'))  # 判断是否为目录
print(os.listdir('.'))  # 列出指定目录下所有内容
# 找出当前目录下所有的文件夹
dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
print(dirs)

# 创建/删除目录
# os.mkdir('world')
if os.path.exists('world'):
    os.rmdir('world')

# 重命名文件或目录
# os.rename('itany.txt', 'aaa.txt')

# 删除文件
# os.remove('aaa.txt')

# 拷贝文件
shutil.copy('baidu.png', 'bbb.png')
```

## 八、访问MySQL

### 1. 简介

​	使用pymysql模块：`pip install pymysql`

### 2. 基本操作

​	增删改

```python
import pymysql

# 定义数据库连接信息
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'python',
    'charset': 'utf8'
}

# 获取连接
conn = pymysql.connect(**config)

# 获取游标，相当于java中的Statement
cursor = conn.cursor()

# 执行sql
sql = '''
    insert into t_user 
      (username,password,age,height)
    values 
      (%s,%s,%s,%s)  
'''
num = cursor.execute(sql, ['alice', '123', 18, 175.2])  # 为占位符%s赋值
print(num)

# 提交事务
conn.commit()

# 关闭资源
cursor.close()
conn.close()
```

​	查询

```python
# 获取游标，相当于java中的Statement
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 可以指定cursor的类型为字典，查询结果为Dict类型

# 执行sql
sql = '''
    select
        id,username,password,age,height
    from t_user    
'''
cursor.execute(sql)

# 获取查询结果
# print(cursor.fetchone()) #　每次读取一条，返回的是元组
# print(cursor.fetchone())
# print(cursor.fetchmany(2))  #  获取多条
# print(cursor.fetchall())  # 获取所有

for u in cursor.fetchall():
    print(u['username'], u['age'])
```



## 九、Flask框架

### 1. 简介

​	常见Python Web框架：

- Flask：是一个使用Python编写的轻量级Web框架，快速开发Web应用
- Django：全能型Web框架，重量级，功能强大

### 2. 第一个Flask程序

​	安装flask：`pip install flask`

​	Flask内置Web服务器，可以直接执行，不需要部署到其他服务器上

```python
from flask import Flask

# 创建一个app，即一个Flask应用
app = Flask(__name__)


# 定义路由，类似于SpringMVC中的@RequestMapping
@app.route('/')
def hello_world():
    return '<h1 style="color:red">Hello World</h1>'


@app.route('/welcome')
def welcome():
    return 'welcome to flask'


# 启动应用
if __name__ == '__main__':
    app.run(port=8888, debug=True)
```

### 3. 请求参数

```python
# Get请求
@app.route('/test_get')
def test_get():
    a = request.args.get('a')
    b = request.args.get('b', default=666)
    print(a, b)
    return 'get'


@app.route('/load_form')
def load_form():
    return '''
        <form action="test_post" method="post">
            a: <input type="text" name="a"> <br>
            b: <input type="text" name="b"> <br>
            <input type="submit" value="提交">
        </form>
    '''


# Post请求
@app.route('/test_post', methods=['post', 'get'])  # 默认只接收GET请求，通过methods指定接收的请求方式
def test_post():
    a = request.form['a']
    b = request.form['b']
    print(a, b)
    return 'post'


# REST风格参数
@app.route('/test_rest/<name>/<int:id>')
def test_rest(name, id):
    print(name, id, type(id))
    return 'rest'
```

### 4. 文件上传

```python
@app.route('/upload', methods=['post'])
def upload():
    # 获取上传的文件
    file = request.files['file']
    # print(type(file)) #　FileStorage类型
    print(file.filename)
    save_path = time.strftime('%Y%m%d%H%M%S') + str(random.randint(1, 100)) + file.filename
    file.save(save_path)
    return 'success'
```

### 5. 响应

```python
from flask import Flask, request, redirect, jsonify
import time
import random
from flask import render_template

app = Flask(__name__)


# 响应html
@app.route('/test_html')
def test_html():
    return '''
        <h1>html</h1>
    '''


# 重定向
@app.route('/test_redirect')
def test_redirect():
    return redirect('/test_html')


# 响应json
@app.route('/test_json')
def test_json():
    user = {'id': 1001, 'name': 'tom', 'age': 18, 'sex': 'male'}
    return jsonify(user)


# 响应模板页
@app.route('/test_template')
def test_template():
    return render_template('hello.html')  # 指定模板文件名，默认在当前目录下的tempaltes中查找
```

### 6. Jinja2模板语法

```python
@app.route('/')
def index():
    name = 'tom'
    age = 81
    users = [
        {'id': 1001, 'name': 'tom', 'age': 18, 'sex': 'male'},
        {'id': 1002, 'name': 'jack', 'age': 28, 'sex': 'female'},
        {'id': 1003, 'name': 'alice', 'age': 38, 'sex': 'male'}
    ]
    return render_template('result.html', username=name, age=age, users=users)
```

```html
<body>
    result.html <br>
    username:{{username}} <br>
    {% if age>60 %}
        老年
    {% elif age>30 %}
        中年
    {% elif age>18 %}
        少年
    {% else %}
        童年
    {% endif %}
    <br>
    <ul>
        {% for user in users %}
            <li>{{user.id}},{{user.name}},{{user.sex}}</li>
        {% endfor %}
    </ul>
</body>
```

### 7. 使用蓝图实现模块化

​	蓝图Blueprint

```python
from flask import Flask
from py07_Flask框架.user_controller import user
from py07_Flask框架.product_controller import product

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user)
app.register_blueprint(product)

if __name__ == '__main__':
    app.run(debug=True)
```

```python
from flask import Blueprint

# 创建蓝图
user = Blueprint('user', __name__)


# 定义蓝图路由
@user.route('/user_list')
def user_list():
    return 'user_list'


@user.route('/user_add')
def user_add():
    return 'user_add'
```









​	