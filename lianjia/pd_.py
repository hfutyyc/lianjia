import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
import pylab as pl


datas = open('home.json', encoding='utf8').readlines()
# print(datas)
place = []
unit_price = []
total_price = []
for data in datas:
    a = json.loads(data)
    if a['unit_price'] and a['total_price']:
        place.append(a['place'])
        unit_price.append(float(a['unit_price']))
        total_price.append(float(a['total_price']))

data_ = {
    'place': place,
    'unit_price': unit_price,
    'total_price': total_price,
}

df = pd.DataFrame(data=data_)

# x = df['place'].str.contains('南山区').fillna(False)
# print(df[x])
# print(df)
# print(df['total_price'].max())
# print(df.min())
place_ = df['place'].value_counts()
print(place_)
print(place_[0])
print(place_[1])
place_.plot(kind='bar', x=place_[0], y=place_[1])
plt.xticks(rotation='horizontal')
plt.title('深圳各区二手房数量')
plt.show()

x_ = df.groupby('place').mean()
# # print(x_)
# # print(x_['unit_price'][3])
# print(list(x_['unit_price'].index))
# print(list(x_['unit_price'][0:11]))
# # place_.plot(kind='bar', x=x_['unit_price'].index, y=x_['unit_price'][0:11])
plt.bar(list(x_['unit_price'].index), list(x_['unit_price'][0:11]))
plt.xticks(rotation='horizontal')
plt.title('深圳各区二手房均价')
plt.show()



