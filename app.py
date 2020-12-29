from flask import Flask, render_template, request, url_for
import tierdatalake.querydatalake as qdl
#from tierdatalake.dataConnection import qDataLakeConn as dc.qDataLakeConn
import tierdatalake.dataConnection as dc

import math

millnames = ['',' Thousand',' Million',' Billion',' Trillion']
def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1, int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

from io import StringIO
import csv
from flask import make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    dominios = dc.qDataLakeConn(qdl.q_ora_domains)
    return render_template('index.html', dominios = dominios)

@app.route('/abastecimiento')
def abastecimiento():
    tablas = dc.qDataLakeConn(qdl.q_ora_abastecimiento_tables)
    return render_template('tableView.html', tablas = tablas)

@app.route('/salud')
def salud():
    tablas = dc.qDataLakeConn(qdl.q_ora_salud_tables)
    return render_template('tableView.html', tablas = tablas)

@app.route('/search', methods=['POST','GET'])
def search():
    if (request.method == "POST"):
        tablename = request.form['query']
        #tablas = dc.qDataLakeConn("""SELECT OWNER,TABLE_NAME,TABLE_LOCK,SAMPLE_SIZE,LAST_ANALYZED FROM ALL_TABLES WHERE TABLE_NAME LIKE '%""" + request.form['query'] + """%'""")
        tablas = dc.qDataLakeConn("""SELECT * FROM SCH_UNIVERSAL.LISTADO_DICCIONARIO WHERE NOMBRE_OBJETO LIKE '%""" + tablename + """%' OR NOMBRE_VARIABLE  LIKE '%""" + tablename + """%'""")
        return render_template('tableView.html', tablas = tablas)
    else:
        return render_template('index.html')

@app.route('/detail/<tablename>')
def detail(tablename):
    #tablas = dc.qDataLakeConn("""SELECT OWNER,TABLE_NAME,COLUMN_NAME,DATA_TYPE,DATA_LENGTH,DATA_PRECISION,COLUMN_ID,NUM_DISTINCT,LOW_VALUE,HIGH_VALUE,DENSITY,NUM_NULLS,LAST_ANALYZED,SAMPLE_SIZE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME LIKE '%""" + tablename + """%'""")
    tablas = dc.qDataLakeConn("""SELECT * FROM SCH_UNIVERSAL.LISTADO_DICCIONARIO WHERE NOMBRE_OBJETO LIKE '%""" + tablename + """%'""")
    tabladescripcion = dc.qDataLakeConn("""SELECT DISTINCT NOMBRE_OBJETO,DESCRIPCION FROM SCH_UNIVERSAL.LISTADO_OBJECT WHERE NOMBRE_OBJETO LIKE '%""" + tablename + """%'""")
    return render_template('columnView.html', tablas = tablas, tabladescripcion = tabladescripcion)


@app.route('/value/<columnname>')
def value(columnname):
    tablas = dc.qDataLakeConn("""SELECT OWNER,TABLE_NAME,COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE COLUMN_NAME LIKE '%""" + columnname + """%'""")
    return render_template('tableView.html', tablas = tablas)


@app.route('/download/<esquema>/<tablename>')
def download(esquema,tablename):
    df = dc.qDataLakeConn("""SELECT * FROM """ + esquema +""".""" + tablename)# + """ WHERE ROWNUM <= 20 """ )
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=muestra_"+ tablename +".csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp

@app.route('/dominio/<nombredominio>')
def dominio(nombredominio):
    if (nombredominio == "None"):
        tablas = dc.qDataLakeConn("""SELECT * FROM SCH_UNIVERSAL.LISTADO_OBJECT WHERE DOMINIO IS NULL""")
    else:
        tablas = dc.qDataLakeConn("""SELECT * FROM SCH_UNIVERSAL.LISTADO_OBJECT WHERE DOMINIO LIKE '%""" + nombredominio + """%'""")
    return render_template('tableView.html', tablas = tablas)