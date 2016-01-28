# -*-coding: utf-8 -*-
from ftplib import FTP
user = 'datum'
passwd = 'BpeTvzw2MM26wp'
#ip = 'ftp.mrsk-yuga.ru'
ip = '192.168.200.10'
head_folder = ['SAP_TOPO', 'СУРР_АВР']
ftp = FTP(host=ip, user=user, passwd=passwd)
#for folder in head_folder:

#        print '*'*15, folder
#        ftp.cwd(folder)
        # ftp.cwd('loaded')
#        ftp.retrlines('LIST')
#        ftp.cwd('..')
#       print '*'*15
# Закрыть соединение
#ftp.quit()
