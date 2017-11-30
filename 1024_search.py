import os
import requests
import re
from bs4 import BeautifulSoup

re_invcode=re.compile(r'[0-9a-z\*\#]{16}')

r = requests.get('http://t66y.com/htm_data/7/1711/2762746.html')
print(r.status_code)
r.encoding ='gbk'
# print(r.text)
# print(r.content)
soup = BeautifulSoup(r.text)
print(soup.get_text())
match_result = re_invcode.findall(soup.get_text())
if match_result:
	print(match_result)
	print(len(match_result))
else:
	print('nothing found')


#os.system( "1024_verify.py %s" % '-C'+'q*###' )


