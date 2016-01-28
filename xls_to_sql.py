def ftb(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    offset = 1
    rows = []
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = []
        for j, col in enumerate(range(sheet_import.ncols)):
            temp_row.append(sheet_import.cell_value(i, j))
        rows.append(temp_row)
    print len(rows)
    f = codecs.open('test.sql', 'wb', encoding='utf-8')
    try:
        for row in rows:
            sql = "INSERT INTO\
 public.sk2007_entity\
 (code,name,type,category)\
 VALUES ({0}, '{1}', '{2}', '{3}');".\
                format(int(row[0]), row[1], row[2], row[3])
            p = u''.join(sql).encode('utf-8').strip()
            # print p.decode('utf-8')
            f.write(p.decode('utf-8') + '\n')
    except Exception, e:
        print 'ERROR'
        print str(e).decode('utf-8')
    f.close()

if __name__ == '__main__':
    ftb('test.xlsx')
