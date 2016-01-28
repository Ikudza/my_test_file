import dbf
table = dbf.Table('temptable', 'name C(30); age N(3,0); birth D')
fileds = ['name', 'age', 'birth']
table.open()
for datum in (
                ('John Doe', 31, dbf.Date(1979, 9,13)),
                ('Ethan Furman', 102, dbf.Date(1909, 4, 1)),
                ('Jane Smith', 57, dbf.Date(1954, 7, 2)),
                ('John Adams', 44, dbf.Date(1967, 1, 9)),
                ):
            table.append(datum)
