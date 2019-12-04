# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/12/3 10:09
# @File     : display.py
# @Software : PyCharm
import preData
from matplotlib import pyplot as plt
import jinja2
from PIL import Image
from pyecharts import Bar


kdaTop, kdaSingle, kdaJungle, kdaAdc, kdaSupport, uziKills, uziSupports, uzidies = preData.loadExcel_2('player.xlsx')
bar = Bar("五个位置KDA历史最高值")
bar.add("KDA", ["上单", "中单", "打野", "射手", "辅助"], [max(kdaTop), max(kdaSingle), max(kdaJungle), max(kdaAdc), max(kdaSupport)])
bar.show_config()
bar.render(path='./data/KDA最高雷达图.html')

bar = Bar("五个位置KDA历史最低值")
bar.add("KDA", ["上单", "中单", "打野", "射手", "辅助"], [min(kdaTop), min(kdaSingle), min(kdaJungle), min(kdaAdc), min(kdaSupport)])
bar.show_config()
bar.render(path='./data/KDA最低雷达图.html')

print("Uzi生涯总击杀数：\n",uziKills)
print("Uzi生涯总助攻数：\n",uziSupports)
print("Uzi生涯总死亡数：\n",uzidies)