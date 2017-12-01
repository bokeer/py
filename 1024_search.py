import os
import requests
import re
from bs4 import BeautifulSoup

re_invcode=re.compile(r'[0-9a-z\*\#\&]{16}')
re_url=re.compile(r'htm_data.*?.html')  
def find_invcode(url):
	s = requests.get(url,timeout=10)
	print(s.status_code)
	s.encoding ='gbk'
	# print(r.text)
	# print(r.content)
	soup = BeautifulSoup(s.text)
	temp_text = soup.get_text().replace('\n','')
	#print(temp_text)
	match_result = re_invcode.findall(temp_text)
	if match_result:
		print(match_result)
		print(len(match_result))
		return 1
	else:
		return 0
		print('nothing found')

#url='http://t66y.com/htm_data/7/1711/2762746.html'

#find_invcode(url)
def find_urlandcode():
	payload = {'fid': '7', 'search': 'today','page':'1'}
	url=r'http://t66y.com/thread0806.php'
	page_num=1
	pre_linklist=[]
	all_url_try=0
	find_state=0
	while True:
		r=requests.get(url,params=payload,timeout=10)
		print(r.url)
		print(r.status_code)
		linklist = re.findall(re_url, r.text)
		for x in range(len(linklist)):
			linklist[x] = r'http://t66y.com/'+linklist[x]
		linklist_set=set(linklist)
		linklist=list(linklist_set)
		print('linklist len:',len(linklist))
		if pre_linklist!=linklist:
			pre_linklist=linklist[:]
		else:
			print('search all new but nothing')
			break
		for url_1 in linklist:
			all_url_try+=1
			print(url_1)
			if find_invcode(url_1):
				print('find',url_1)
				find_state=1
				if find_state==1:
					console=input()
					if console=='':
						print('next')
						find_state=0
					else:
						print('exit')
						break
		if find_state==1:
			break
		page_num+=1
		payload['page']=str(page_num)
	print('all_url_try:',all_url_try)	


find_urlandcode()
#os.system( "1024_verify.py %s" % '-C'+'q1')

