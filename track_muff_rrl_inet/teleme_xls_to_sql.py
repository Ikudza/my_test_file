# -*- coding: utf-8 -*-
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import LineString
import sys
from uuid import uuid4


def to_geom(point):
    point = point.split('), (')
    try:
        points = []
        for point_ in point:
            point_ = point_
            point_ = point_.split(', ')
            for i in xrange(len(point_)):
                point_[i] = point_[i].strip(u' ("\u0412\u0421).')
                point_[i] = point_[i].split(u"'")
                point_[i][0:0] = point_[i][0].split(u'\xb0')
                del point_[i][2]
                point_[i] = float(point_[i][0]) +\
                    (float(point_[i][1]) +
                     float(point_[i][2])/60)/60

            point_ = Point(point_[1], point_[0])
            points.append(point_)
        geom = LineString(*points)

    except:
        return None
    return geom.wkt


def to_point(coord):
    point_ = coord.split(', ')
    try:
        for i in xrange(len(point_)):
            point_[i] = point_[i].strip(u' "\u0412\u0421')
            point_[i] = point_[i].split(u"'")
            point_[i][0:0] = point_[i][0].split(u'\xb0')

            del point_[i][2]
            point_[i] = float(point_[i][0]) +\
                (float(point_[i][1]) +
                 float(point_[i][2])/60)/60
    except:
        if point_[0][0] == u'нет данных':
            return None
    point_ = Point(point_[0], point_[1])
    return point_.wkt


def ftb_track(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    offset = 2
    rows = []
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = []
        temp_row.append('{%s}' % str(uuid4()).upper())
        for j, col in enumerate(range(sheet_import.ncols)):
            #  For track
            if j == 3:
                temp_row.append(to_geom(sheet_import.cell_value(i, j)))
            elif j == 4 or j == 5 or j == 6 or j == 7 or\
                    j == 8 or j == 9 or j == 10:
                value = sheet_import.cell_value(i, j)
                if value:
                    temp_row.append(value)
                else:
                    temp_row.append(0.0)
            else:
                try:
                    temp_row.append(unicode(sheet_import.cell_value(i, j)))
                except:
                    temp_row.append(sheet_import.cell_value(i, j))
        rows.append(temp_row)
    print len(rows)
    try:
        f = codecs.open('track_.sql', 'a', encoding='utf-8')
    except:
        f = codecs.open('track_.sql', 'wb', encoding='utf-8')
    try:
        for row in rows:
            sql = u"('guid':  u'{0}', 'filial': u'{1}', 'division': u'{2}', \
'name': u'{3}', 'length_line': '{4}', \
'length_optics': '{5}', 'gasket':'{6}', 'height': '{7}', \
'count_fiber': '{8}', 'count_replace_fiber': '{9}', \
'count_used_fiber': '{10}', 'geom': u'{11}')\
".format(row[0], row[1], row[2], row[3], row[5], row[6],
         row[7], row[8], row[9], row[10], row[11], row[4])

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


def func_recur(func, i, j):
    if i == 2 or func(i, j):
        return func(i, j)
    return func_recur(func, i-1, j)


def ftb_muff(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    offset = 2
    rows = []
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = []
        temp_row.append('{%s}' % str(uuid4()).upper())
        for j, col in enumerate(range(sheet_import.ncols)):
            #  For muff
            if j < 3 and not sheet_import.cell_value(i, j):
                temp_row.append(func_recur(sheet_import.cell_value, i, j))
            elif j == 4:
                x = sheet_import.cell_value(i, j)
                y = sheet_import.cell_value(i, j+1)
                if x and y and not(u'нет' in x):
                    temp_row.append(to_point(x + ', ' + y))
                else:
                    temp_row.append(None)
            elif j == 5:
                pass
            else:
                value = sheet_import.cell_value(i, j)
                try:
                    temp_row.append(unicode(value))
                except:
                    temp_row.append(value)
        rows.append(temp_row)
    print len(rows)
    try:
        f = codecs.open('muff_.sql', 'a', encoding='utf-8')
    except:
        f = codecs.open('muff_.sql', 'wb', encoding='utf-8')
    try:
        for i, row in enumerate(rows):
            sql = u"('guid': '{0}', 'filial': '{1}', 'division': '{2}', \
'name_fiber': '{3}', 'name_muff': '{4}', 'type_place': '{5}', 'height': '{6}', \
'type': '{7}', 'count_fiber': '{8}', 'count_fiber_stock': '{9}', \
'count_fiber_use': '{10}', 'geom': u'{11}'),\
".format(row[0], row[1], row[2], row[3], row[4], row[6],
         row[7], row[8], row[9], row[10], row[11], row[5])

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


def to_line_rrl(x, y, x_1, y_1):
    try:
        if u'В.Д.' in x:
            result = []

            for t in [x, y, x_1, y_1]:
                temp_X = t.split(" ")
                del temp_X[0]
                result.append(float(temp_X[0].strip()) +
                             (float(temp_X[1].strip()) + float(temp_X[2].replace(',', '.'))/60)/60)
        else:
            result = []
            for t in [x, y, x_1, y_1]:
                if u'\u2019' in t:
                    temp_X = t.strip(u'\u201d ').split(u"\u2019")
                elif u'\u2032' in t:
                    temp_X = t.strip(u'\u2032 ').split(u"\u2032")
                else:
                    temp_X = t.strip(u'\u0421\u0412" ').split("'")
                if u'\xb0' in temp_X[0]:
                    temp_X[0:0] = temp_X[0].split(u'\xb0')
                elif u'\u043e' in temp_X[0]:
                    temp_X[0:0] = temp_X[0].split(u'\u043e')
                else:
                    temp_X[0:0] = temp_X[0].split(u'o')
                del temp_X[2]
                result.append(float(temp_X[0].strip()) + (float(temp_X[1].strip()) + float(temp_X[2].strip())/60)/60)
    except:
        import traceback; traceback.print_exc();
        import sys
        print sys.exc_info()
        import pdb; pdb.set_trace()
    geom = LineString(Point(result[0], result[1]),
                      Point(result[2], result[3]))
    return geom.wkt


def ftb_rrl(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    offset = 2
    rows = []
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = []
        temp_row.append('{%s}' % str(uuid4()).upper())
        for j, col in enumerate(range(sheet_import.ncols)):
            #  For rrl
            if j < 2:
                temp_row.append(func_recur(sheet_import.cell_value, i, j))
            elif j == 3:
                x = sheet_import.cell_value(i, j)
                y = sheet_import.cell_value(i, j+1)
                x_1 = sheet_import.cell_value(i, j+2)
                y_1 = sheet_import.cell_value(i, j+3)
                if x and y:
                    temp_row.append(to_line_rrl(x, y, x_1, y_1))
                else:
                    temp_row.append(None)
            elif j in [4, 5, 6]:
                pass
            else:
                value = sheet_import.cell_value(i, j)
                try:
                    temp_row.append(unicode(value))
                except:
                    temp_row.append(value)
        rows.append(temp_row)
    print len(rows)
    try:
        f = codecs.open('rrl_.sql', 'a', encoding='utf-8')
    except:
        f = codecs.open('rrl_.sql', 'wb', encoding='utf-8')
    try:
        for i, row in enumerate(rows):
            sql = u"('guid': '{0}', 'filial': '{1}', 'division': '{2}', \
'name_rrl': '{3}', 'spring': '{4}', 'azimuth_1': '{5}', 'height_1': '{6}', \
'height_sea_1': '{7}', 'azimuth_2': '{8}', 'height_2': '{9}', \
'height_sea_2': '{10}', 'size': '{11}', 'frequency_range': '{12}', \
'gain_tx': '{13}', 'power_tx': '{14}', 'losses': '{15}', 'receiv_lvl': '{16}', \
'capacity': '{17}', 'geom': u'{18}'),\
".format(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8],
         row[9], row[10], row[11], row[12], row[13], row[14], row[15],
         row[16], row[17], row[18], row[4])

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


def ftb_inet(filename):
    import codecs
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    offset = 2
    rows = []
    for i, row in enumerate(range(sheet_import.nrows)):
        if i < offset:
            continue
        temp_row = []
        temp_row.append('{%s}' % str(uuid4()).upper())
        for j, col in enumerate(range(sheet_import.ncols)):
            #  For inet
            if j < 2:
                temp_row.append(func_recur(sheet_import.cell_value, i, j))
            elif j == 3:
                x = sheet_import.cell_value(i, j)
                y = sheet_import.cell_value(i, j+1)
                x_1 = sheet_import.cell_value(i, j+2)
                y_1 = sheet_import.cell_value(i, j+3)
                if x and y:
                    temp_row.append(to_line_rrl(x, y, x_1, y_1))
                else:
                    temp_row.append(None)
            elif j in [4, 5, 6]:
                pass
            else:
                value = sheet_import.cell_value(i, j)
                try:
                    temp_row.append(unicode(value))
                except:
                    temp_row.append(value)
        rows.append(temp_row)
    print len(rows)
    try:
        f = codecs.open('inet_.sql', 'a', encoding='utf-8')
    except:
        f = codecs.open('inet_.sql', 'wb', encoding='utf-8')
    try:
        for i, row in enumerate(rows):
            sql = u"('guid': '{0}', 'filial': '{1}', 'division': '{2}', \
'name_fiber': '{3}', 'spring': '{4}', 'azimuth_1': '{5}', 'azimuth_2': '{6}', \
'frequency_range': '{7}', 'band': '{8}', 'modulation': '{9}', \
'number_threads': '{10}', 'geom': u'{11}'),\
".format(row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8],
         row[9], row[10], row[11], row[4])

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


def delete_file(line_name):
    import os
    for name in line_name:
        try:
            os.remove(name)
        except:
            pass


if __name__ == '__main__':
    delete_file(['track_.sql', 'muff_.sql', 'rrl_.sql', 'inet_.sql'])
    ftb_track('test_track.xlsx')
    ftb_track('test_track (1).xlsx')
    ftb_track('test_track (2).xlsx')
    ftb_track('test_track (3).xlsx')
    ftb_muff('test_muff (1).xlsx')
    ftb_muff('test_muff (2).xlsx')
    ftb_muff('test_muff (3).xlsx')
    ftb_muff('test_muff (4).xlsx')
    ftb_rrl('test_rrl (1).xls')
    ftb_rrl('test_rrl (2).xlsx')
    ftb_inet('test_inet (1).xlsx')
    ftb_inet('test_inet (2).xlsx')
