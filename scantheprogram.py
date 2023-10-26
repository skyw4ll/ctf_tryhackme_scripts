#!/usr/bin/env python3


import subprocess


command = '/root/tmp/psychobreak/program {}'

file = open('/root/tmp/psychobreak/random.dic', 'r')

for line in file:
    output = subprocess.check_output(command.format(line), shell=True)
    result = output.decode('UTF-8').rstrip()

    if 'Incorrect' not in result:
        print('Found ==> ' + line)
        print(result)
        break

