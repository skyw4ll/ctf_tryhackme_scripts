#!/usr/bin/env python3


import requests


url = 'http://10.10.76.78/api/'
flag = ''

tmpUrl = url

for i in range(10, 100):
    tmpUrl = url + str(i)

    data = requests.get(tmpUrl).json()

    item_id = data['item_id']
    q = data['q']

    print(f"id : {item_id} --- q : {q}")

    flag = q

    if q != 'Error. Key not valid!':
        break

print("\nFLAG : " + flag)

