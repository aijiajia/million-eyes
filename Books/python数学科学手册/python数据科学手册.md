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
### 1.4 IPython魔法命令
### 1.5 禁止输出
### 1.6 IPython和shell命令
### 1.7 与shell有关的魔法命令
### 1.8 错误和调试
### 1.9 代码的分析和记时
### 1.10 IPython参考资料