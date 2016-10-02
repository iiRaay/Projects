import sqlite3

sqlite_file = '/Users/Ray/Desktop/SQLiteTest/my_db.sqlite'

table_name1 = 'my_table1'
table_name2 = 'my_table2'

new_field = 'my_1st_column'
field_type = 'INTEGER'

# connect to database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# create a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=new_field, ft=field_type))

#create a second table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name2, nf=new_field, ft=field_type))

# commits changes and closes connection to database file
conn.commit()
conn.close()