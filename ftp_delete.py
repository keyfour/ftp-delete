#!/usr/bin/env python
#
# Copyright (c) Aleksandr Karpov <keyfour13@gmail.com>
#
import argparse
from ftplib import FTP

parser = argparse.ArgumentParser(description='Delete files via FTP.')
parser.add_argument('-l', '--login', required = True, help='FTP login')
parser.add_argument('-p', '--passwd', required = True, help='FTP password')
parser.add_argument('-u', '--url', required  = True, help='FTP URL')
parser.add_argument('-d', '--delete', required = True, help='Delete path')
args = parser.parse_args()

ftp = FTP(host=args.url,user=args.login,passwd=args.passwd)

def delete(path):
    ftp.cwd(path)
    files = ftp.nlst()
    d = ftp.pwd()

    if files == None or len(files) == 0:
        ftp.cwd('../')
        ftp.rmd(d)
        if d == args.delete:
            return
    else:
        for f in reversed(files):
            try:
                ftp.delete(f)
                files.remove(f)
                print("%s deleted" % f)
                delete(d)
            except:
                print("%s is directory" % f)
                delete(f)


delete(args.delete)

