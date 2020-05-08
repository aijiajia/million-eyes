# encoding: utf-8
"""
@author: monitor1379 
@contact: herbert_git@163.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: 第一个例子.py
@time: 2020/5/7 5:16 PM

这一行开始写关于本文件的说明与解释
"""

import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
# hash
import hashlib

from sklearn.model_selection import train_test_split

from sklearn.model_selection import StratifiedShuffleSplit

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


def run():
    print(HOUSING_URL)


# 第一步 获取数据
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# 第一步 获取数据-创建测试集（方法一随机数）缺点：每次随机后的数据不同


def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


# train_set, test_set = split_train_test(housing, test_ratio=0.2)
# print("train len : ", len(train_set), "  test len : ", len(test_set))

# 第一步 获取数据-创建测试集 方法二使用哈希 缺点，每次随机后虽然相同，但是不能保证分层采样比例


def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

# housing_with_id = housing.reset_index()   # adds an `index` column
# train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

# 如果使用行索引作为唯一识别码，你需要保证新数据放到现有数据的尾部，且没有行被深处。如果做不到，则可以用最稳定的特征来创建唯一识别码。例如，一个区的维度和经度在几百万年之内是不变的，所以可以将两者结合成一个ID
# housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
# train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

# 第一步 获取数据-创建测试集 方法三  Scikit-Learn提供的函数
# train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42) 这种方法仍然不能解决分层采样

# housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
# >=5 的值都被替换成5，小于5的没事
# housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
#
# split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
# for train_index, test_index in split.split(housing, housing["income_cat"]):
#     strat_train_set = housing.loc[train_index]
#     strat_test_set = housing.loc[test_index]
# strat_test_set["income_cat"].value_counts() / len(strat_test_set)
# housing["income_cat"].value_counts() / len(housing)


def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)


# train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
#
# compare_props = pd.DataFrame({
#     "Overall": income_cat_proportions(housing),
#     "Stratified": income_cat_proportions(strat_test_set),
#     "Random": income_cat_proportions(test_set),
# }).sort_index()
# compare_props["Rand. %error"] = 100 * compare_props["Random"] / compare_props["Overall"] - 100
# compare_props["Strat. %error"] = 100 * compare_props["Stratified"] / compare_props["Overall"] - 100
#
# compare_props





if __name__ == '__main__':
    # fetch_housing_data()
    housing = load_housing_data()
    print(housing.head())
    print(housing['ocean_proximity'].values)
    # print(housing['ocean_proximity'].value_counts())
    # print(housing.info())
    # print(housing.describe())
    # housing.hist(bins=50, figsize=(20, 15))
    # plt.show()
    # imputer = Imputer(strategy="median")
    # housing_num = housing.drop("ocean_proximity", axis=1)
    # imputer.fit(housing_num)
    # print(imputer.statistics_)
    # X = imputer.transform(housing_num)
    # housing_tr = pd.DataFrame(X, columns=housing_num.columns)
    # print(housing_tr.info())
    encoder = LabelEncoder()
    housing_cat = housing['ocean_proximity']
    housing_cat_encoded = encoder.fit_transform(housing_cat)
    print(housing_cat_encoded.shape)
    print(housing_cat_encoded.reshape(-1, 1))
    # print(housing_cat_encoded)
    # encoder_one_hot_encoder = OneHotEncoder()
    # housing_cat_1hot = encoder_one_hot_encoder.fit_transform(housing_cat_encoded.reshape(-1,1))
