import requests
import string
hidecode='**pqawsr1sqdaaaw'
print('hidecode len:',len(hidecode))
decode={'*':'num','&':'character','#':'n&c'}
decode_dic={}  #查询到特殊符号及其索引
decode_list=[]  #每个特殊符号可以替换的种类
decode_index_list=[]  #每个特殊符号的位置索引

num_list=[]
character_list=[]
nc_list=[]
for x in range(10):
	num_list.append(chr(48+x))
for x in range(26):
	character_list.append(chr(97+x))
for x in range(36):
	if x < len(num_list):
		nc_list.append(chr(48+x))
	else:
		nc_list.append(chr(48+39+x))
# print('num_list:',num_list)
# print('character_list:',character_list)
# print('nc_list:',nc_list)
num_sum=len(num_list)
character_sum=len(character_list)
nc_sum=len(nc_list)

for x in range(len(hidecode)):
	for k,v in decode.items():
		if hidecode[x] == k:
			decode_dic[x] = v
			decode_index_list.append(x)

possible_count=1
for v in decode_dic.values():
	if v=='num':
		possible_count*=num_sum
		decode_list.append(num_sum)
	elif v=='character':
		possible_count*=character_sum
		decode_list.append(character_sum)
	else:
		possible_count*=nc_sum
		decode_list.append(nc_sum)

print('decode_dic:',decode_dic)
print('decode_list:',decode_list)
print('decode_index_list:',decode_index_list)
symbol_count=len(decode_dic)
print('symbol_count:',symbol_count)
print('possible_count:',possible_count)


possible_list=[]
# g=(x for x in range(10,50))
# w=(x for x in range(30,50))
# print(next(g))
# print(next(w))


'''
计算所有可能性，存在possible_list中
combination(0)
'''
def combination(t):
	# global time_s #全局变量在函数中调用时加 global
	if t == symbol_count:
		return True
	if t == 0:
		if decode_list[t]==num_sum:
			for x in range(decode_list[t]):
				possible_list.append(num_list[x])
		elif decode_list[t]==character_sum:
			for x in range(decode_list[t]):
				possible_list.append(character_list[x])
		elif decode_list[t]==nc_sum:
			for x in range(decode_list[t]):
				if x < num_sum:
					possible_list.append(num_list[x])
				else:
					possible_list.append(character_list[x])
		else:
			pass
	else:
		tmp_list = possible_list[:] #tmp_list = possible_list 引用的是同一内存地址的list
		# print('tmp_list:',tmp_list)
		# print(len(tmp_list))
		if decode_list[t]==num_sum:
			for q in range(decode_list[t]):
				if q == 0:
					for x in range(len(tmp_list)):
						possible_list[x] += num_list[q]
				else:
					for x in range(len(tmp_list)):
						possible_list.append(tmp_list[x]+num_list[q])
		elif decode_list[t]==character_sum:
			for q in range(decode_list[t]):
				if q == 0:
					for x in range(len(tmp_list)):
						possible_list[x] += character_list[q]
				else:
					for x in range(len(tmp_list)):
						possible_list.append(tmp_list[x]+character_list[q])
		elif decode_list[t]==nc_sum:
			for q in range(decode_list[t]):
				if q == 0:
					for x in range(len(tmp_list)):
						possible_list[x] += nc_list[q]
				else:
					for x in range(len(tmp_list)):
						possible_list.append(tmp_list[x]+nc_list[q])
		else:
			pass
	return combination(t+1)
def httprequest(invcode):
	payload = {'reginvcode':invcode, 'action': 'reginvcodeck'}
	# proxies = {
	#   'http': '10.10.1.10:3128',
	#   'https': '10.10.1.10:1080',
	# }
	# r = requests.get('http://example.org', proxies=proxies)
	r = requests.post('http://t66y.com/register.php?',data = payload)
	#print(payload)
	print(r.status_code)
	r.encoding ='gbk'
	#print(s.text)
	if r.text=="<script language=\"JavaScript1.2\">parent.retmsg_invcode('1');</script>":
		print('yes')
	#print(r.text)

if symbol_count > 0:
	combination(0)
else:
	print('没有特殊字符')
print('possible_list len:',len(possible_list))

target_string=''
target_code=list(hidecode)

for x in range(possible_count):          #possible_count 默认是1
	for x_1 in range(symbol_count):
		target_code[decode_index_list[x_1]]=possible_list[x][x_1]
		target_string=''.join(target_code) 
	#print(target_string)
	#httprequest(target_string)



