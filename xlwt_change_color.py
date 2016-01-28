from xlwt import Workbook
import xlwt
book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
book.add_sheet('Sheet 2')
st = xlwt.easyxf('pattern: pattern solid;')
for i in range(0, 100):
    st.pattern.pattern_fore_colour = 2
    sheet1.write(i % 24, i / 24, 'Test text',st)
book.save('simple.xls')
