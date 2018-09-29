# Python数据科学手册

## 第1章 IPython：超越Python

### 1.1 shell还是Notebook

#### 1.1.1 启动IPthon shell
```ipython```
#### 1.1.2 启动Jupyter Notebook
```jupyter notebook```

### 1.2 IPython的帮助文档
IPython 和 Jupyter 最大的用处之一就是能缩短用户与帮助文档和搜索间的距离， 帮助用户高效完成工作。 虽然网络搜索在解答复杂问题时非常
有用， 但是仅仅使用 IPython 就能找到大量的信息了。 以下是仅通过几次按键， IPython 就可以帮你解答的一些问题。

#### 1.2.1 用符号?获取文档
- Python 内置的 help() 函数可以获取这些信息， 并且能
打印输出结果。 例如， 如果要查看内置的 len 函数的文档， 可以按照以下步骤操作：
```
// docstring
In [3]: help(len)
Help on built-in function len in module builtins:

len(obj, /)
```
- 获取关于一个对象的帮助非常常见， 也非常有用， 所以 IPython 引入了 ? 符号作为获取这个文档和其他相关信息的缩写：
```
In [4]: len?
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method
```
- 这种表示方式几乎适用于一切， 包括对象方法：
```
In [5]: str.count?
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      method_descriptor
```
- 甚至对于对象本身以及相关类型的文档也适用：
```
In [6]: L=[1,3,4]

In [7]: L?
Type:        list
String form: [1, 3, 4]
Length:      3
Docstring:
list() -> new empty list
list(iterable) -> new list initialized from iterable's items
```

#### 1.2.2 通过符号??获取源码
```
In [11]: def add(a,b):
    ...:     '''return a plus b'''
    ...:     return a+b
    ...:

In [12]: add?
Signature: add(a, b)
Docstring: return a plus b
File:      d:\projects\github_projects\million-eyes35\<ipython-input-11-74101caf660d>
Type:      function

In [13]: add??
Signature: add(a, b)
Source:
def add(a,b):
    '''return a plus b'''
    return a+b
File:      d:\projects\github_projects\million-eyes35\<ipython-input-11-74101caf660d>
Type:      function
```
#### 1.2.3 用Tab补全的方式探索模块
- 01.对象内容的Tab自动补全
- 02.导入时的Tab自动补全
```
In [10]: from itertools import co<TAB>
```
- 03.超越Tab自动补全： 通配符匹配
当你知道所寻找的对象或属性的第一个或者前几个字符时， Tab 自动补全将非常有用。 但是当你想匹配中间或者末尾的几个字符时， 它就
束手无策了。 对于这样的场景， IPython 提供了用 * 符号来实现的通配符匹配方法。
例如， 可以用它列举出命名空间中以 Warning 结尾的所有对象：
```
In [14]: *Warning?
BytesWarning
DeprecationWarning
FutureWarning
ImportWarning
PendingDeprecationWarning
ResourceWarning
RuntimeWarning
SyntaxWarning
UnicodeWarning
UserWarning
Warning
```
同理， 假设我们在寻找一个字符串方法， 它的名称中包含 find， 则可以这样做：
```
In [10]: str.*find*?
str.find
str.rfind
```

### 1.3 IPython shell的快捷键
#### 1.3.1 导航快捷键
| 快捷键   | 动作      |
| -------- | --------- |
| Ctrl + a | 行首      |
| Ctrl + e | 结尾      |
| Ctrl + b | 回退1字符 |
| Ctrl + f | 前进1字符 |
####  1.3.2 文本输入快捷键
| 快捷键    | 动作                           |
| --------- | ------------------------------ |
| Backspace | 删除前一个字符                 |
| Ctrl + d  | 删除后一个字符                 |
| Ctrl + k  | 从光标开始剪切至行的末尾       |
| Ctrl + u  | 从行的开头剪切至光标           |
| Ctrl + y  | yank（即粘贴） 之前剪切的文本  |
| Ctrl + t  | transpose（即交换） 前两个字符 |
#### 1.3.3 命令历史快捷键
| 快捷键                 | 动作                 |
| ---------------------- | -------------------- |
| Ctrl + p（或向上箭头） | 获取前一个历史命令   |
| Ctrl + n（或向下箭头)  | 获取后一个历史命令   |
| Ctrl + r               | 对历史命令的反向搜索 |

【重要】你可以随时添加更多的字符来重新定义搜索， 或者再一次按下 Ctrl + r 键来寻找另外一个匹配该查询的命令。 如果你在前一节中照做了的话，
按下 Ctrl + r 键两次将可以看到：
```
In [1]:
(reverse-i-search)`sqa': def square(a):
"""Return the square of a"""
return a ** 2
```

找到你在寻找的命令后， 按下 Return 键将会终止查找。 然后就可以利用查找到的命令， 继续我们的会话：

#### 1.3.4 其他快捷键
| 快捷键   | 动作                   |
| -------- | ---------------------- |
| Ctrl + l | 清除终端屏幕的内容     |
| Ctrl + c | 中断当前的 Python 命令 |
| Ctrl + d | 退出 IPython 会话      |

### 1.4 IPython魔法命令
行魔法（line magic） 和单元魔法（cell magic） 。 行魔法以单个 % 字符作为前缀， 作用于单行输入； 单元魔法以两个 %% 作为
前缀， 作用于多行输入。
#### 1.4.1  %paste和%cpaste
【重要，复制时带有些杂七杂八的代码也可以】IPython 的 %paste 魔法函数可以解决这个包含符号的多行输入问题
#### 1.4.2 执行外部代码:%run
```
In [6]: %run myscript.py
1 squared is 1
2 squared is 4
3 squared is 9
```
#### 1.4.3 计算代码运行时间:%timeit
%timeit 的好处是， 它会自动多次执行简短的命令， 以获得更稳定的结果。 对于多行语句， 可以加入第二个 % 符号将其转变成单元魔法， 以处
理多行输入。 例如， 下面是 for 循环的同等结构
```
In [33]: %%timeit
    ...: L=[]
    ...: for n in range(1000):
    ...:     L.append(n ** 2)
    ...:
1000 loops, best of 3: 379 µs per loop
```
#### 1.4.4 魔法函数的帮助： ?、 %magic和%lsmagic

### 1.5 禁止输出
### 1.6 IPython和shell命令
### 1.7 与shell有关的魔法命令
Notebook 中的 shell 命令是在一个临时的分支 shell 中执行的。 如果你希望以一种更持久的方式更改工作路径， 可以使用 %cd 魔法命令：
```
In [37]: !dir
 驱动器 D 中的卷是 DATA
 卷的序列号是 EAA8-2B02

 D:\projects\github_projects\million-eyes35 的目录

2018/07/25  12:02    <DIR>          .
2018/07/25  12:02    <DIR>          ..
2018/09/13  15:35    <DIR>          .idea
2018/09/13  11:32    <DIR>          Books
2018/07/25  12:02    <DIR>          Docs
2018/07/25  12:02               566 README.md
               1 个文件            566 字节
               5 个目录 177,028,411,392 可用字节

In [38]: %cd Books/
D:\projects\github_projects\million-eyes35\Books

In [39]: %cd ..
D:\projects\github_projects\million-eyes35

In [40]: !dir
 驱动器 D 中的卷是 DATA
 卷的序列号是 EAA8-2B02

 D:\projects\github_projects\million-eyes35 的目录

2018/07/25  12:02    <DIR>          .
2018/07/25  12:02    <DIR>          ..
2018/09/13  15:35    <DIR>          .idea
2018/09/13  11:32    <DIR>          Books
2018/07/25  12:02    <DIR>          Docs
2018/07/25  12:02               566 README.md
               1 个文件            566 字节
               5 个目录 177,016,647,680 可用字节

```
### 1.8 错误和调试
### 1.9 代码的分析和记时
### 1.10 IPython参考资料
## 第2章 NumPy入门
### 2.1 理解Python中的数据类型
### 2.2 NumPy数组基础
### 2.3 NumPy数组的计算：通用函数
### 2.4 聚合：最小值、最大值和其他值
### 2.5 数组的计算：广播
### 2.6 比较、掩码和布尔逻辑
| 运算符 | 对应的通用函数   |
| ------ | ---------------- |
| ==     | np.equal         |
| ！=    | np.not_equal     |
| <      | np.less          |
| <=     | np.less_equal    |
| >      | np.greater       |
| >=     | np.greater_equal |
### 2.7 花哨的索引
### 2.8 数组的排序
### 2.9 结构化数据：NumPy的结构化数组
- [numpy np.newaxis 的实用](https://www.cnblogs.com/onemorepoint/p/8110523.html)
## 第3章 Pandas数据处理
### 3.1 安装并使用Pandas
### 3.2 Pandas对象简介

### 3.3 数据取值与选择
### 3.4 Pandas数值运算方法
### 3.5 处理缺失值
### 3.6 层级索引
### 3.7 合并数据集：Concat与Append操作
### 3.8 合并数据集：合并与连接
### 3.9 累计与分组
### 3.10 【??】数据透视表
### 3.11 向量化字符串操作
### 3.12 处理时间序列
### 3.13 高性能Pandas：eval()与query()
### 3.14 参考资料
## 第4章 Matplotlib数据可视化
### 4.1 Matplotlib常用技巧
### 4.2 两种画图接口
### 4.3 简易线形图
### 4.4 简易散点图
## 第5章 机器学习
### 5.1 什么是机器学习
### 5.2 Scikit-Learn简介
 ![image]()
### 5.3 超参数与模型验证
### 5.4 特征工程
### 5.5 朴素贝叶斯分类
### 5.6 线性回归
### 5.7 支持向量机
### 5.8 决策树与随机森林
### 5.9 主成分分析
### 5.10 流式学习
### 5.11 k-means聚类
### 5.12 高斯混合模型
### 5.13 核密度估计
### 5.14 人脸识别管道
### 5.15 机器学习参考资料