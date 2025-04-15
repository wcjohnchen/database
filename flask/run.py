from flask import Flask, render_template, request

import numpy as np
import pandas as pd

import psycopg2
import psycopg2.extras

app = Flask(__name__)


@app.route('/') # Homepage
def home():
    return render_template('index.html')



@app.route('/query',methods=['POST'])
def query():

    if request.method == 'POST':

        genename = request.form.get('gene')


        hostname = '' # <--- enter hostname
        database = '' # <--- enter database name
        username = '' # <--- enter username
        pwd = '' # <--- enter password
        port_id =  # <--- enter port id
        conn = None
        tablename= 'polyadb4_lr' # <--- enter table name

        try:
            with psycopg2.connect(
                host = hostname,
                dbname = database,
                password = pwd,
                port = port_id) as conn:
            
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:


                    if genename == 'LIST':
                        cur.execute(f"SELECT DISTINCT(gene_symbol) FROM {tablename} ORDER BY gene_symbol ASC")
                        data = cur.fetchall()
                        conn.commit()                  
                    elif "," not in genename:
                        genename = genename.strip()
                        cur.execute(f"SELECT * FROM {tablename} WHERE gene_symbol = '{genename}' ORDER BY type_main ASC")
                        data = cur.fetchall()
                        conn.commit()
                    else:
                        list = [item.strip() for item in genename.split(",")]       
                        list=tuple(list)
                        cur.execute(f"SELECT * FROM {tablename} WHERE gene_symbol IN {list} ORDER BY gene_symbol ASC, type_main ASC")
                        data = cur.fetchall()
                        conn.commit()




        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    
    
    
    if len(data) == 0:
        return render_template('index.html', queries='No Data')
        
    elif genename == 'LIST':
        headings = ['Gene Symbol']
        return render_template('index.html', headings=headings, data=data)
        
    else:
        headings = ['Key', 'Gene Symbol', 'PasID', 'Type', 'PSE', 'AvgRPM', 'mm10_pAid', 'NumRefSeq', 'NumLRENCODE', 'NumLRGETx', 'polyAID', 'polyAStrength', 'SVM']
        return render_template('index.html', headings=headings, data=data)



if __name__ == '__main__':
    app.run(debug=True)

