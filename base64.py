#!/usr/bin/env python3


import base64

f = open('/root/tmp/scripting/b64.txt', 'r')
code = f.read()

for i in range(50):
    code = base64.b64decode(code)

print(code)

