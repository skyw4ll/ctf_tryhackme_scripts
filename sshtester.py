#!/usr/bin/env python3


import subprocess
import threading


url = '10.10.149.24'
username = 'root'

blackList = [9100, 9101, 9102, 9103, 9104, 9105, 9106, 9107]
command = 'ssh {} -l {} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o HostkeyAlgorithms=+ssh-rsa -p {}'
higherList = []
threads = []
portIndex = 12600  # 9000
portOffset = 100  # sum 14000
threadCount = 10


def checkssh(startIndex, finishIndex):
    for port in range(startIndex, finishIndex):

        if port in blackList:
            continue

        output = subprocess.check_output(command.format(url, username, str(port)), shell=True)

        result = output.decode('UTF-8').rstrip()

        if len(result) > 7:
            higherList.append(str(port) + ' is right port. You got it!!!')


def main():
    increaseValue = int(portOffset / threadCount)
    tmpStartIndex = portIndex
    tmpFinishIndex = portIndex + increaseValue
    for t in range(threadCount):
        t = threading.Thread(target=checkssh, args=(tmpStartIndex, tmpFinishIndex, ))
        threads.append(t)
        t.start()
        tmpStartIndex = tmpFinishIndex
        tmpFinishIndex += increaseValue

    for t in threads:
        t.join()

    for item in higherList:
        print(item)


if __name__ == '__main__':
    main()

