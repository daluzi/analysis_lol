# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/12/23 19:52
# @File     : teamDataPro.py
# @Software : PyCharm

import numpy as np
from openpyxl import load_workbook
import pandas as pd


def loadExcel_2(filename):
	workbook = load_workbook(filename)
	# booksheet = workbook.active                #获取当前活跃的sheet,默认是第一个sheet
	sheets = workbook.get_sheet_names()  # 从名称获取sheet
	booksheet = workbook.get_sheet_by_name(sheets[0])

	rows = booksheet.rows
	columns = booksheet.columns
	KDATop = []
	KDASingle = []
	KDAAdc = []
	KDAJungle = []
	KDASupport = []
	uziAllKill = 0
	uziAllSup = 0
	uziAllDie = 0
	uziKDA = {}
	# 迭代所有的行
	for row in rows:
		line = [col.value for col in row]
		if line[15] == 'IM':
			print(line)


	KDATop = list(map(float, KDATop))
	KDASingle = list(map(float, KDASingle))
	KDAAdc = list(map(float, KDAAdc))
	KDAJungle = list(map(float, KDAJungle))
	KDASupport = list(map(float, KDASupport))



	return KDATop, KDASingle, KDAAdc, KDAJungle, KDASupport, uziAllKill, uziAllSup, uziAllDie, uziKDA



if __name__ == '__main__':
	filename = './team.xlsx'
	# loadExcel_2(filename)
	data = pd.DataFrame(pd.read_excel(filename))
	# for i in range(0, 3861):
	# 	if data['战队 '][2] != 'RNG ' or data['战队 '][2] != 'IG ' or data['战队 '][2] != 'OMG ' or data['战队 '][2] != 'WE ' or data['战队 '][2] != 'EDG ' or data['战队 '][2] != 'LGD ':
	# 		data.drop([i])
	# 		# print(data)
	# print(data)
	# print(data['战队 '][2])
	# print(data.loc[data['战队 '] == 'RNG'].index)
	# for i in range(0, len(np.array(data.loc[data['战队 '] == 'RNG']))):
	# 	print(np.array(data.loc[data['战队 '] == 'RNG'])[i][2])
	# for i in range(0, len(np.array(data.loc[data['战队 '] == 'IG']))):
	# 	print(np.array(data.loc[data['战队 '] == 'IG'])[i][1])
	# for i in range(0, len(np.array(data.loc[data['战队 '] == 'OMG']))):
	# 	print(np.array(data.loc[data['战队 '] == 'OMG'])[i][1])
	# for i in range(0, len(np.array(data.loc[data['战队 '] == 'WE']))):
	# 	print(np.array(data.loc[data['战队 '] == 'WE'])[i][1])
	# for i in range(0, len(np.array(data.loc[data['战队 '] == 'EDG']))):
	# 	print(np.array(data.loc[data['战队 '] == 'EDG'])[i][1])
	for i in range(0, len(np.array(data.loc[data['战队 '] == 'LGD']))):
		print(np.array(data.loc[data['战队 '] == 'LGD'])[i][1])
