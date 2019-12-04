# _*_ coding: utf-8 _*_
# @Author   : daluzi
# @time     : 2019/12/3 17:23
# @File     : paqu1.py
# @Software : PyCharm

from urllib import parse
import urllib.request
import threading


# 使用多线程爬取

def loadPage(url, filename):
	'''
		作用：根据url发送请求，获取服务器响应文件
		url:需要爬取的url地址
		filename:文件名
	'''
	print('正在下载', filename)

	ua_headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
	}
	# 构建请求对象
	request = urllib.request.Request(url, headers=ua_headers)
	respond = urllib.request.urlopen(request)  # 返回类文件对象
	print(respond.getcode())
	html = respond.read()

	print('正在保存', filename)
	with open(filename, 'w') as f:
		f.write(html)


def writePage(html, filename):
	'''
		作用：将html页面写入本地磁盘中
		html：所爬取的网页
		filename:保存的文件名
	'''
	print('正在保存', filename)
	with open(filename, 'w') as f:
		f.write(html)


def webSpider(url, begin_page, end_page):
	'''
		作用: 负责处理url，分配每个url去发送请求
		url:需要去处理的第一个url
		begin_page:起始页
		end_page:终止页
	'''
	for page in range(begin_page, end_page + 1):
		pn = (page - 1) * 50

		filename = '第' + str(page) + '页.html'

		full_url = url + '&pn=' + str(pn)  # 组合完整的url
		# print(full_url)
		t = threading.Thread(target=loadPage, args=(full_url, filename))
		t.start()


if __name__ == '__main__':
	while True:
		kw = input('请输入你要爬取的贴吧关键字:').strip()
		beginPage = input('起始页：').strip()
		endPage = input('终止页：').strip()

		if (kw and beginPage and endPage):
			word = parse.urlencode({'kw': kw})  # 转换为url编码
			url = 'http://tieba.baidu.com/f?'
			new_url = url + word  # 组合后的url，示例;http://tieba.baidu.com/f?kw=lol

			webSpider(new_url, int(beginPage), int(endPage))
			break