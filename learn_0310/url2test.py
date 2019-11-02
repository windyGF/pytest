import urllib.request
import os
import ssl
import json
import random
context = ssl._create_unverified_context()

proxy_IP = ['119.6.144.73:81',]

proxy_support = urllib.request.ProxyHandler({'http':random.choice(proxy_IP)})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15')
	response = urllib.request.urlopen(req, context=context)
	
	print('status:', response.status, response.reason)
	
	for k, v in response.getheaders():
		print('%s: %s' % (k, v))
	
	html = response.read()
	
	return html

if __name__ == '__main__':
	content = url_open('https://api.douban.com/v2/book/2129650')
	print('Data:',json.loads(content.decode('utf-8')))


