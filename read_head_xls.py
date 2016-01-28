def ftb(filename):
    import xlrd
    file_import = xlrd.open_workbook(filename)
    sheet_import = file_import.sheet_by_index(0)
    for i, row in enumerate(range(sheet_import.nrows)):
        for j, col in enumerate(range(sheet_import.ncols)):
            print sheet_import.cell_value(i, j).lower()
            print ';'
        break

if __name__ == '__main__':
    ftb(u'test.xlsx')
