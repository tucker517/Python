'''
Created on Feb 27, 2020

@author: JTC

This  script ingests random data created using the api data generator in this folder.
This excercise demonstrates how data can be piped into a database using effecient python code.
'''

import requests.get
import psycopg2.connect

with requests.get("http://XXXXXX/very_large_request/1000XXXXXXX", stream=True) as r:
    conn = psycopg2.connect(dbname="test_db",
                            user="[XXXX]",
                            password="[XXXX]")
    cur = conn.cursor()
    sql = "INSERT INTO transactions (txid, uid, amount) VALUES (%s, %s, %s)"


    buffer = ""
    for chunk in r.iter_content(chunk_size=1):
        if chunk.endswith(b'\n'):
            t = eval(buffer)
            print(t)
            cur.execute(sql, (t[0], t[1], t[2]))
            conn.commit()
            buffer = ""
        else:
            
            buffer += chunk.decode()
