# -*- coding: utf-8 -*-
import datetime

dict_avr = {u'ДЗО': u'dzo',
            u'Филиал': u'filial',
            u'ПО (РЭС)': 'departament',
            u'Место': u'place_save',
            u'Принадлежность': u'view',
            u'Класс': u'class_equip',
            u'Наименов': u'name_equip',
            u'напряжения': u'class_voltage',
            u'Тип': u'type_equip',
            u'Ед.': u'measure',
            u'Факт': u'fact_coint',
            u'Нормат': u'nominal_coint',
            u'к пополнению': u'need_coint',
            u'Учетная ': u'carrying_amount',
            u'Рыночная': u'market_price',
            u'Состояние': u'condition',
            u'Должность': u'position',
            u'ФИО': u'full_name',
            u'Контакты': u'contacts',
            u'Примечание': u'note',
            u'Плановый': u'planned_term',
            u'Пояснения': u'notes_completion'}


def float_to_date(value):
    value = float(value)
    start_date = datetime.datetime(1899, 12, 30)
    value = start_date + datetime.timedelta(value)
    return value.strftime('%d.%m.%Y')


def ftb_storage(filename, max_):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    if 'ros' in filename:
        level = u'Россети'
        try:
            name = u'ОАО "МРСК Юга"'
            sheet_import = file_import.sheet_by_name(name)
            k = 3
        except:
            # import pdb; pdb.set_trace()
            pass
    else:
        level = u'МРСК'
        sheet_import = file_import.sheet_by_index(0)
        k = 2
    offset = k+1
    rows = []
    print filename, sheet_import.ncols
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = {}
        temp_row['level'] = level
        # temp_row['id'] = i
        for j, col in enumerate(range(sheet_import.ncols)):
            if j == 0:
                continue
            value = sheet_import.cell_value(i, j)
            head_ = sheet_import.cell_value(k, j)
            if not head_:
                head_ = sheet_import.cell_value(k-1, j)
            if not head_:
                continue
            for key in dict_avr:
                if key in head_:
                    head = dict_avr[key]
                    break
            try:
                temp_row[head] = value.strip(u' \n')
            except UnboundLocalError:
                # import pdb; pdb.set_trace()
                pass
            except:
                temp_row[head] = str(value)
        space = False
        if len(temp_row) < 21:
            temp_row_key = temp_row.keys()
            dict_avr_val = dict_avr.values()
            for key in dict_avr_val:
                if not(key in temp_row_key):
                    temp_row[key] = ''

        counter = 1
        len_temp = len(temp_row)
        for key in temp_row.keys():
            if not(temp_row[key]):
                counter += 1
        if len_temp == counter:
            space = True
        if space:
            continue
        rows.append(temp_row)

    try:
        f = codecs.open('__result.sql', 'a', encoding='utf-8')
        # f = codecs.open('_%s.sql' % filename, 'a', encoding='utf-8')
    except:
        f = codecs.open('__result.sql', 'wb', encoding='utf-8')
        # f = codecs.open('_%s.sql' % filename, 'wb', encoding='utf-8')
    for i, row in enumerate(rows):
        if row[u'planned_term']:
            try:
                row[u'planned_term'] = float_to_date(row[u'planned_term'])
            except:
                pass
        sql = u"            %s," % row
        max_ = _max_length(max_, row)
        # print p.decode('utf-8')
        f.write(unicode(sql + '\n'))
    f.close()
    return max_


def delete_file(line_name):
    import os
    for name in line_name:
        try:
            os.remove(name)
        except:
            pass


def _max_length(max_, dict_):
    for k in dict_:
        len_ = len(dict_[k])
        try:
            if max_[k] < len_:
                max_[k] = len_
        except:
            max_[k] = len_
    return max_


if __name__ == '__main__':
    delete_file(['_Aros.xlsx.sql', '_Amrsk.xlsx.sql',
                 '_Kros.xlsx.sql', '_Kmrsk.xlsx.sql',
                 '_Vros.xlsx.sql', '_Vmrsk.xlsx.sql',
                 '_Rros.xlsx.sql', '_Rmrsk.xlsx.sql',
                 '__result.sql'])
    max_ = {}
    max_ = ftb_storage('Aros.xlsx', max_)
    max_ = ftb_storage('Amrsk.xlsx', max_)
    max_ = ftb_storage('Kros.xlsx', max_)
    max_ = ftb_storage('Kmrsk.xlsx', max_)
    max_ = ftb_storage('Vros.xlsx', max_)
    max_ = ftb_storage('Vmrsk.xlsx', max_)
    max_ = ftb_storage('Rros.xlsx', max_)
    max_ = ftb_storage('Rmrsk.xlsx', max_)
    for k in max_:
        print k, max_[k]
