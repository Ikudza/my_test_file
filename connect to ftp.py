# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xlrd
from ftplib import FTP
user = 'datum'
passwd = 'BpeTvzw2MM26wp'
ip = '192.168.200.10'
ftp = FTP(host=ip, user=user, passwd=passwd)
ftp.cwd("SAP_TOPO")
ftp.cwd('loaded')
ftp.cwd('PS')
fs = ftp.nlst('')
f = fs[0]
