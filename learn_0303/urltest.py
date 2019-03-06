import urllib.request
import os
import ssl

context = ssl._create_unverified_context()

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15')
	response = urllib.request.urlopen(req, context=context)
	print('status:', response.status, response.reason)
	html = response.read()
	return html
if __name__ == '__main__':
	content = url_open('http://www.douban.com/')
#	print('status:',content.statrs,content.reason)
	print('Data:',content.decode('utf-8')[0:100])


