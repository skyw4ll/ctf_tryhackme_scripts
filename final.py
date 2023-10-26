#!/usr/bin/env python3


import os
import mmap
import zipfile
import exiftool


path = '/root/tmp/advent2019/final'
count = 0


def unzipfiles(extpath):
    global count, path
    files = os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filepath = os.path.join(path, file)
            zip_file = zipfile.ZipFile(filepath, 'r')
            for names in zip_file.namelist():
                zip_file.extract(names, path + '/' + extpath)
                count += 1
            zip_file.close()


def findversion(word):
    global count, path
    files = os.listdir(path)
    for file in files:
        try:
            with exiftool.ExifToolHelper() as et:
                metadata = et.get_metadata(os.path.join(path, file))
                for meta in metadata:
                    if 'XMP:Version' in meta:
                        if repr(meta['XMP:Version']) == word:
                            count += 1
        except:
            pass


def findtext(word):
    global count, path
    files = os.listdir(path)
    for file in files:
        filepath = os.path.join(path, file)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:
            lines = txt.readlines()
            for line in lines:
                if word in line:
                    file_name = os.path.basename(filepath)
                    text = line.replace('\n', '')
                    print(f"{file_name} --- Word '{word}' found on line {lines.index(line)} --- {text}")
                    count += 1
                    break


def findtextwithmmap(word):
    global count, path
    files = os.listdir(path)
    for file in files:
        filepath = os.path.join(path, file)
        with open(filepath, 'rb', 0) as txt:
            m = mmap.mmap(txt.fileno(), 0, access=mmap.ACCESS_READ)
            if m.find(word) != -1:
                file_name = os.path.basename(filepath)
                print(f"{file_name} --- Word '{word}' found")
                count += 1


def main():
    global count, path

    zipsdir = path + '/zips'
    metadatasdir = zipsdir + '/metadatas'

    if not os.path.exists(zipsdir):
        os.makedirs(zipsdir)

    if not os.path.exists(metadatasdir):
        os.makedirs(metadatasdir)

    unzipfiles('zips')
    print(f'extract zips count : {count}')

    path = zipsdir
    count = 0
    unzipfiles('metadatas')
    print(f'extract metadatas count : {count}')

    path = metadatasdir
    count = 0
    findversion('1.1')
    print(f'version found count : {count}')

    count = 0
    findtext('password')
    print(f'password found count : {count}')

    count = 0
    findtextwithmmap(b'password')
    print(f'password found with mmap count : {count}')


if __name__ == '__main__':
    main()

