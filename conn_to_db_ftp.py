# -*- coding: utf-8 -*-
import pyodbc

path_to_db = u'D:/sphera_krasnodar/New26082008/ARX_DB'

cnxn = pyodbc.connect(r"Driver={{Microsoft Paradox Driver (*.db )\}};DriverID=538;Fil=Paradox 5.X;DefaultDir={0};Dbq={0};CollatingSequence=ASCII;".format(path_to_db), autocommit=True, readonly=True)
cursor = cnxn.cursor()
cursor.execute("select * from jurnal")
row = cursor.fetchone()
print row
import pdb; pdb.set_trace()
