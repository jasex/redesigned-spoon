import nation
import province
import 应届往届 as yin
import 户口 as hu
import name
import Ewrite

def generate():
    list=[]
    natio=nation.pick_nation()
    list.append(natio)
    provinc=province.pick_province()
    list.append(provinc)
    yi=yin.pick_yin()
    list.append(yi)
    h=hu.pick_hu()
    list.append(h)
    nam=name.create_name()
    list.append(nam)
    return list

list=[]
for i in range(200):
    stu=generate()
    list.append(stu)
Ewrite.writeExcel(list)
