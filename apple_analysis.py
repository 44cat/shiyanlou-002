# -*- coding:utf-8 -*-
import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    #print(data.Volume) 会带上索引输出
    #print(data.Date) 会带上索引输出
    Volume_datas = data.Volume
    Date_datas = data.Date
    #用成交日期创建当天成交量时间戳索引
    Volume_datas.index = pd.to_datetime(Date_datas)
    #print(Volume_datas)
    
    second_valume = Volume_datas.resample('Q').sum().sort_values()[-2]
    #print(s)
    #print(type(s))
    return second_valume
    
if __name__ == "__main__":
    quarter_volume()
