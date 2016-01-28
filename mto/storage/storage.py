# -*- coding: utf-8 -*-
import datetime
import sys


def float_to_date(value):
    start_date = datetime.datetime(1899, 12, 30)
    value = start_date + datetime.timedelta(value)
    return value.strftime('%d.%m.%Y')


def join_certif(func, i, j):
    value = func(i, j)
    if isinstance(value, (float, int)):
        value = float_to_date(value)
    temp = func(i, j+1).split(u' ')
    try:
        temp[2] = u' '.join([u'№', temp[2]])
    except:
        temp[1] = temp[1][:2] + u' № ' + temp[1][2:]
    temp = u' '.join(temp)
    value = u' от '.join([temp, value])
    return value


def ftb_storage(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    for z in range(file_import.nsheets):
        sheet_import = file_import.sheet_by_index(z)
        offset = 2
        rows = []
        for i, row in enumerate(range(sheet_import.nrows)):
            if i < offset:
                continue
            temp_row = []
            for j, col in enumerate(range(sheet_import.ncols)):
                if sheet_import.ncols == 4:
                    if j == 0 or i == 2:
                        continue
                    if j == 3:
                        temp_row.append(' ')
                        value = sheet_import.cell_value(i, j)
                if sheet_import.ncols == 9:
                    if j == 4:
                        value = sheet_import.cell_value(i, 8)
                        temp_row.append(value)
                        value = sheet_import.cell_value(i, j)
                    elif j == 6:
                        value = join_certif(sheet_import.cell_value,
                                            i, j)
                    elif j in [7, 8]:
                        continue
                    else:
                        value = sheet_import.cell_value(i, j)
                else:
                    if j == 4:
                        value = ' '
                        temp_row.append(value)
                    value = sheet_import.cell_value(i, j)
                try:
                    if sheet_import.ncols == 4:
                        if j == 1:
                            temp_row.append(int(float(value)))
                        else:
                            temp_row.append(unicode(value.strip(u'\n')))
                    else:
                        if j == 0:
                            temp_row.append(int(float(value)))
                        else:
                            temp_row.append(unicode(value.strip(u'\n')))
                except:
                    temp_row.append(value.strip(u'\n'))
            if len(temp_row) < 8:
                while len(temp_row) < 8:
                    temp_row.append(' ')
            rows.append(temp_row)

        try:
            f = codecs.open('storage_.sql', 'a', encoding='utf-8')
        except:
            f = codecs.open('storage_.sql', 'wb', encoding='utf-8')
        try:
            for i, row in enumerate(rows):
                sql = u"('code': '{0}', 'name_1c': '{1}', 'filial': '{2}', \
'address': '{3}', 'address_legal': '{4}', 'full_name': '{5}', \
'name_obj': '{6}', 'certif_doc': '{7}'),\
".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

                sql = u''.join(sql).strip()
                # print p.decode('utf-8')
                f.write(unicode(sql + '\n'))
        except Exception, e:
            print 'ERROR'
            import traceback; traceback.print_exc();
            print str(e).decode('utf-8')

            import pdb
            pdb.set_trace()
        f.close()
        pass


def delete_file(line_name):
    import os
    for name in line_name:
        try:
            os.remove(name)
        except:
            pass


if __name__ == '__main__':
    delete_file(['storage_.sql'])
    ftb_storage('test_ (2).xlsx')
    ftb_storage('test_ (1).xlsx')
