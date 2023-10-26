#!/usr/bin/env python3


import requests


url = 'http://10.10.169.100:3000/'
i = 0
flag = ''

tmpUrl = url

while i < 1:
	data = requests.get(tmpUrl).json()

	nextt = data['next']
	value = data['value']

	print('url : ' + tmpUrl + ' --- next : ' + nextt + ' --- value : ' + value)

	tmpUrl = url + nextt

	if nextt == 'end' and value == 'end':
		i = 1
		break

	flag += value

print('\nFLAG : ' + flag)

