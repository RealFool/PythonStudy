#!/usr/bin/python
# -*- encoding: utf-8

import numpy as np
import pandas as pd
# 字符串模糊匹配
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def enum_row(row):
    print(row['state'])


def find_state_code(row):
    if row['state'] != 0:
        # 找80分以上的
        print(process.extractOne(row['state'], states, score_cutoff=80))


def capital(str):
    # 首字母转大写，其余小写
    return str.capitalize()


def correct_state(row):
    if row['state'] != 0:
        # 提取相似度最高的一位
        state = process.extractOne(row['state'], states, score_cutoff=80)
        if state:
            # 替换成标准库里的
            state_name = state[0]
            """
            map函数也是python中的一个内置函数，用法同之前讲过的filter函数类似。
            map在这里的意思是映射的意思，会根据提供的函数对指定序列做映射。
            map函数会返回一个迭代器，如果要转换为列表，可以使用 list() 来转换。
            """
            return ' '.join(map(capital, state_name.split(' ')))
    return row['state']


def fill_state_code(row):
    if row['state'] != 0:
        state = process.extractOne(row['state'], states, score_cutoff=80)
        if state:
            state_name = state[0]
            return state_to_code[state_name]
    return ''


if __name__ == "__main__":
    # 输出的数据一行可显示的长度
    pd.set_option('display.width', 200)
    data = pd.read_excel('.\\sales.xlsx', sheet_name='sheet1', header=0)
    # 输出文件头，data.head()默认前5行
    print('data.head() = \n', data.head())
    # 输出文件尾
    print('data.tail() = \n', data.tail())
    # 数据类型
    print('data.dtypes = \n', data.dtypes)
    print('data.columns = \n', data.columns)
    for c in data.columns:
        print(c, end=' ')
    print()
    data['total'] = data['Jan'] + data['Feb'] + data['Mar']
    print(data.head())
    print(data['Jan'].sum())
    print(data['Jan'].min())
    print(data['Jan'].max())
    print(data['Jan'].mean())

    print('=============')
    # 添加一行
    s1 = data[['Jan', 'Feb', 'Mar', 'total']].sum()
    print(s1)
    s2 = pd.DataFrame(data=s1)
    print(s2)
    print(s2.T)
    # 自定义fill_value=0，默认填充NaN
    print(s2.T.reindex(columns=data.columns, fill_value=0))
    # 即：
    s = pd.DataFrame(data=data[['Jan', 'Feb', 'Mar', 'total']].sum()).T
    s = s.reindex(columns=data.columns, fill_value=0)
    print(s)
    # 合并连接，默认axis=0行合并
    data = pd.concat([data, s], ignore_index=True, axis=0)
    # 修改索引名字
    data = data.rename(index={15: 'Total'})
    print(data.tail())

    # apply的使用，枚举，axis=1表示x轴按行遍历，0按列遍历
    print('==============apply的使用==========')
    data.apply(enum_row, axis=1)

    # 定义一个标准库，用来做数据矫正的标准
    state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU",
                     "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI",
                     "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID",
                     "FEDERATED STATES OF MICRONESIA": "FM",
                     "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL",
                     "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT",
                     "MASSACHUSETTS": "MA",
                     "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD",
                     "NEW MEXICO": "NM",
                     "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO",
                     "Armed Forces Middle East": "AE",
                     "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA",
                     "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI",
                     "MARSHALL ISLANDS": "MH",
                     "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV",
                     "LOUISIANA": "LA",
                     "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI",
                     "NORTH DAKOTA": "ND",
                     "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY",
                     "RHODE ISLAND": "RI",
                     "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}
    states = list(state_to_code.keys())
    # ratio() 字符串相似度， 字符串编辑距
    print(fuzz.ratio('Python Package', 'PythonPackage'))
    # process.extract() Mississippi在states{}中相似度匹配
    print(process.extract('Mississippi', states))
    # limit=1 限定最匹配的那一个
    print(process.extract('Mississipi', states, limit=1))
    print(process.extractOne('Mississipi', states))
    # 数据集中的数据与标准库中的数据相似度匹配
    print('数据集中的数据与标准库中的数据相似度匹配-----------')
    data.apply(find_state_code, axis=1)

    # 数据校正前
    print('数据校正前 State:\n', data['state'])
    data['state'] = data.apply(correct_state, axis=1)
    # 数据矫正后
    print('数据矫正后 State:\n', data['state'])
    data.insert(5, 'State Code', np.nan)
    data['State Code'] = data.apply(fill_state_code, axis=1)
    print(data)

    # group by，分组查询
    print('==============group by================')
    print(data.groupby('State Code'))
    print('All Columns:\n')
    print(data.groupby('State Code').sum())
    print('Short Columns:\n')
    print(data[['State Code', 'Jan', 'Feb', 'Mar', 'total']].groupby('State Code').sum())

    # 写入文件
    # # data.to_excel('sales_result.xls', sheet_name='Sheet1', index=False)
    # # 从 openpyxl 模块，导入Workbook类
    # from openpyxl import Workbook
    # # 工作簿是文档所有其他部分的容器
    # book = Workbook()
    # # 始终使用至少一个工作表创建一个工作簿
    # sheet = book.active
    # # 使用dataframe_to_rows方法将数据添加到表中
    # from openpyxl.utils.dataframe import dataframe_to_rows
    #
    # for row in dataframe_to_rows(data, index=False, header=True):
    #     sheet.append(row)
    # # 写入内容
    # book.save("sales_result.xls")
