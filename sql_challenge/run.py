
import os

from init_db import init_db

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
sql_query = open(os.path.join(__location__, 'sql_query.sql'))

with init_db() as cur:
    sql_as_string = sql_query.read()
    cur.execute(sql_as_string)

    rows = cur.fetchall()

    for row in rows:
        print(row)
