#!/usr/bin/env python3


import binascii
import pickle


f = open('/root/tmp/peakhill/creds', 'r').read()

bytes = binascii.unhexlify('%x' % int(f, 2))

output = dict(pickle.loads(bytes))

username = ''
password = ''

for i in range(7):
    username += output[f'ssh_user{i}']

for i in range(28):
    password += output[f'ssh_pass{i}']

print('Username: ' + username)
print('Password: ' + password)

