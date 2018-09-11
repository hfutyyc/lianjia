#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import json
import csv


def json_to_csv():
    datas = open("home.json", "r", encoding='utf8').readlines()
    json_file = []
    for data in datas:
        try:
            data = dict(data)
            if data['unit_price'] and data['total_price']:
                json_file.append(data)
        except Exception:
            pass
    # print(str(json_file))
    # with open('home_.json', 'w', encoding='utf8')as f:
    #     f.write(str(json_file))
    # json_file = open('home_.json', 'w', encoding='utf8')
    print(json_file)
    csv_file = open("home.csv", "w")

    #  [{}, {}, {}]
    result_list = dict(json_file)

    #[key, key, key]
    #[value, value]
    #[(key, value), (key, value)]

    # [head, head, head]
    sheet_head = result_list[0].keys()

    #sheet_data = []
    #for result in result_list:
    #    sheet_data.append(result.values())

    #[[], [], []]
    sheet_data = [result.values() for result in result_list]

    # csv文件读写对象，负责对指定的csv文件进行数据读写
    csv_writer = csv.writer(csv_file)

    # 先写一行表头[]
    csv_writer.writerow(sheet_head)
    # 再写多行表数据 [[], []]
    csv_writer.writerows(sheet_data)

    csv_file.close()
    json_file.close()


if __name__ == "__main__":
    json_to_csv()
