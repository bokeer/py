import os
import requests
import re
from bs4 import BeautifulSoup
default_timeout=20
re_invcode=re.compile(r'[0-9a-zA-Z\*\#\&]{16}')
re_url=re.compile(r'htm_data.*?.html')  
def find_invcode(url):
	s = requests.get(url,timeout=default_timeout)
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
	invalid_url_list=[]
	try:
		with open('invalid_url.txt', 'r') as fr:
		    for line in fr.readlines():
		    	invalid_url_list.append(line.strip())
	except IOError:
		print('file not exist')
	print('invalid_url_list len:',len(invalid_url_list))
	payload = {'fid': '7', 'search': 'today','page':'1'}
	url=r'http://t66y.com/thread0806.php'
	page_num=1
	pre_linklist=[]
	all_url_try=0
	find_state=0
	while True:
		r=requests.get(url,params=payload,timeout=default_timeout)
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
			print('all_url_try ',all_url_try)
			print(url_1)
			if find_invcode(url_1):
				print('find',url_1)
				if url_1 not in invalid_url_list:
					console=input()
					if console=='':
						try:
							with open('invalid_url.txt', 'a') as fw:
								fw.write(url_1+'\n')
						except IOError:
							print('file write failed')
						print('next')
					else:
						find_state=1
						print('exit')
						break
		if find_state==1:
			break
		page_num+=1
		payload['page']=str(page_num)
	print('all_url_try:',all_url_try)	


find_urlandcode()
#os.system( "1024_verify.py %s" % '-C'+'q1')

