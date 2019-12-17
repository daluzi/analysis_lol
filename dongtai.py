# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/12/17 16:52
# @File     : dongtai.py
# @Software : PyCharm
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# y1 = []
# for i in range(50):
#     y1.append(i)  # 每迭代一次，将i放入y1中画出来
#     ax.cla()   # 清除键
#     ax.bar(y1, label='test', height=y1, width=0.3)
#     ax.legend()
#     plt.pause(0.1)



# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.axis([0, 100, 0, 1])
# plt.ion()
#
# xs = [0, 0]
# ys = [1, 1]
#
# for i in range(100):
#     y = np.random.random()
#     xs[0] = xs[1]
#     ys[0] = ys[1]
#     xs[1] = i
#     ys[1] = y
#     plt.plot(xs, ys)
#     plt.pause(0.1)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

overdoses = pd.read_excel('overdose_data_1999-2015.xls', sheet_name='Online', skiprows=6)
def get_data(table, rownum, title):
	data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
	data.columns = {title}
	return data

title = 'Heroin Overdoses'
d = get_data(overdoses, 18, title)
x = np.array(d.index)
y = np.array(d['Heroin Overdoses'])
overdose = pd.DataFrame(y, x)
overdose.columns = {title}

# Writer = animation.writers['ffmpeg']
# Writer = Writer(fps = 20, metadata = dict(artist = 'Me'), bitrate = 1800)

fig = plt.figure(figsize=(10, 6))
plt.xlim(1999, 2016)
plt.ylim(np.min(overdose)[0], np.max(overdose)[0])
plt.xlabel('Year', fontsize = 20)
plt.ylabel(title, fontsize = 20)
plt.title('Heroin Overdoses per Year', fontsize = 20)

def animate(i):
	data = overdose.iloc[:int(i + 1)]
	p = sns.lineplot(x = data.index, y = data[title], data = data, color = 'r')
	p.tick_params(labelsize = 17)
	plt.setp(p.lines, linewidth = 7)

ani = matplotlib.animation.FuncAnimation(fig, animate, frames = 17, repeat=True)
# ani.save('HeroinOverdosesJumpy.mp4', writer = Writer)
plt.show()