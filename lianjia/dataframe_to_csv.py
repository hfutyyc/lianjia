import json
import pandas as pd


datas = open('home.json', encoding='utf8').readlines()
# print(datas)
room = []
title = []
place = []
unit_price = []
total_price = []
area = []
communityName = []
for data in datas:
    a = json.loads(data)
    if a['unit_price'] and a['total_price']:
        title.append(a['title'])
        place.append(a['place'])
        communityName.append(a['communityName'])
        unit_price.append(float(a['unit_price']))
        total_price.append(float(a['total_price']))
        room.append(a['room'])
        area.append(a['area'])

data_ = {
    'title': title,
    'place': place,
    'communityName': communityName,
    'unit_price': unit_price,
    'total_price': total_price,
    'room': room,
    'area': area,
}

df = pd.DataFrame(data=data_)
print(df)
df.to_csv('home.csv', encoding='utf-8')

