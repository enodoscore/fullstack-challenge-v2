import csv
import os
import sqlite3
from contextlib import contextmanager

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def load_data(file_name, table_name, cursor):
    with open(os.path.join(__location__, file_name),'r') as fin:
        dr = csv.DictReader(fin)
        table_columns = ', '.join(dr.fieldnames)
        create_statement = "CREATE TABLE {} ({});".format(table_name, table_columns)
        cursor.execute(create_statement)
        to_db = [[i[col] for col in dr.fieldnames] for i in dr]
        values = ' ,'.join(['?' for _ in dr.fieldnames])
        cursor.executemany("INSERT INTO {} ({}) VALUES ({});".format(table_name, table_columns, values), to_db)

@contextmanager
def init_db():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    load_data('DepartmentA.csv', 'deptA', cur)
    load_data('DepartmentB.csv', 'deptB', cur)
    
    conn.commit()
    yield cur
    conn.close()

