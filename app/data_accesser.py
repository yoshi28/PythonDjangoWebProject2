import json
import psycopg2
import psycopg2.extras

def get_data():
    # connect postgreSQL
    users = 'postgres'
    dbnames = 'henpin'
    passwords = 'ysaknkd2822'
    conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords)

    # excexute sql
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT id, type, name FROM henpin.henpindata;')
    results = cur.fetchall()

    dict_result = []
    for row in results:
        dict_result.append(dict(row))

    cur.close()
    conn.close()

    return dict_result