# -*- coding: utf-8 -*-
# @Time    : 2022-10-30 11:17
# @Author  : wuhongda
# @Email   : wuhongda@jumstc.com
# @File    : select_data.py
# @Software: PyCharm

import pandas as pd
#读取数据
path1 = "D:\project\py\PythonTaskLearning\pandas_exercise\exercise_data\chipotle.tsv"
tbl = pd.read_csv(path1, sep='\t')

# print(tbl.head(10))
'''
   order_id  ...  item_price
0         1  ...      $2.39 
1         1  ...      $3.39 
2         1  ...      $3.39 
3         1  ...      $2.39 
'''

# print(tbl.shape[1])

# print(tbl.columns)
'''
Index(['order_id', 'quantity', 'item_name', 'choice_description','item_price'],dtype='object')
'''

# sum_agg = tbl[['item_name','quantity']].groupby(['item_name']).agg({'quantity':sum})
# print(sum_agg)
'''
item_name                                   quantity
Barbacoa Bowl                                66
Barbacoa Burrito                             91
Barbacoa Crispy Tacos                        12
'''

# sum_cols = tbl['quantity'].sum()
# print(sum_cols)
'''
4972
'''

# count_distinct = tbl['item_name'].nunique()
# print(count_distinct)
'''
50
'''

# groupby_distinct = tbl['choice_description'].value_counts().head
# print(groupby_distinct)
'''
[Coke]                                                                                                                                           123
[Sprite]                                                                                                                                          77
[Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Lettuce]]                                                                            42
[Fresh Tomato Salsa, [Rice, Black Beans, Cheese, Sour Cream, Guacamole, Lettuce]] 
'''


dollarizer = lambda x : float(x[1:-1])
tbl['item_price'] = tbl['item_price'].apply(dollarizer)
print(tbl.head(10))
'''
del_doller_word
   order_id  ...  item_price
0         1  ...        2.39
1         1  ...        3.39
'''