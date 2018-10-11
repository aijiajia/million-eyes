#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 第五章.py
@time: 2018/9/29 15:29
"""


def demo01():
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    iris = sns.load_dataset('iris')
    print(iris.head())
    sns.pairplot(iris, hue='species', size=1.5)
    plt.show()


def demo02():
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    iris = sns.load_dataset('iris')
    print(iris.head())
    print(iris.shape)
    X_iris = iris.drop('species', axis=1)
    print(X_iris.head())
    print(X_iris.shape)
    y_iris = iris['species']
    print(y_iris.head())
    print(y_iris.shape)


def demo03():
    import matplotlib.pyplot as plt
    import numpy as np
    rng = np.random.RandomState(42)
    x = 10 * rng.rand(50)
    y = 2 * x - 1 + rng.randn(50)
    plt.scatter(x, y)
    plt.show()


# np.random.randn(size)所谓标准正太分布（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)
def demo04():
    import matplotlib.pyplot as plt
    import numpy as np
    rng = np.random.RandomState(42)
    x = np.linspace(1, 50, 50)
    print(x)
    y = rng.randn(50)
    plt.plot(x, y)
    plt.show()


def demo05():
    import matplotlib.pyplot as plt
    import numpy as np
    rng = np.random.RandomState(42)
    x = 10 * rng.rand(50)
    X = x[:, np.newaxis]
    y = 2 * x - 1 + rng.randn(50)
    from sklearn.linear_model import LinearRegression
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    print(model.coef_)
    print(model.intercept_)
    xfit = np.linspace(-1, 11)
    Xfit = xfit[:, np.newaxis]
    yfit = model.predict(Xfit)
    plt.scatter(x, y)
    plt.plot(xfit, yfit)
    plt.show()


def iris():
    from sklearn.cross_validation import train_test_split
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    iris = sns.load_dataset('iris')
    print(iris.head())
    print(iris.shape)
    X_iris = iris.drop('species', axis=1)
    # print(X_iris.head())
    # print(X_iris.shape)
    y_iris = iris['species']
    # print(y_iris.head())
    # print(y_iris.shape)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)
    from sklearn.naive_bayes import GaussianNB  # 1.选择模型类
    model = GaussianNB()  # 2.初始化模型
    model.fit(Xtrain, ytrain)  # 3.用模型拟合数据
    y_model = model.predict(Xtest)  # 4.对新数据进行预测
    from sklearn.metrics import accuracy_score
    print(accuracy_score(ytest, y_model))


if __name__ == '__main__':
    iris()
