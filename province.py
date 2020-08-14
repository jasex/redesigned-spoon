#! /usr/bin/env python3
import time
import random

data={'河北省':1,'山西省':1,'辽宁省':1,'吉林省':1,'黑龙江省':1,'江苏省':1,'浙江省':1,'安徽省':1,'福建省':1,'江西省':1,'山东省':1,'河南省':1,'湖北省':1,'湖南省':1,'广东省':1,'海南省':1,'四川省':1,'贵州省':1,'云南省':1,'陕西省':1,'甘肃省':1,'青海省':1,'台湾省':1,'内蒙古自治区':1,'广西壮族自治区':1,'西藏自治区':1,'宁夏回族自治区':1,'新疆维吾尔自治区':1,'北京市':40,'天津市':1,'上海市':1,'重庆市':1,'香港特别行政区':1,'澳门特别行政区':1}
def pick_province():
    value_list=[]
    for key,value in data.items():
         value_list+=value*[key]
    pick_value=random.choice(value_list)
    return pick_value
