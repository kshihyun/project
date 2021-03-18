
import pymysql
import os
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/result', methods=['GET','POST'])
def db_connector():

    if request.method == 'POST':
            value = request.form['location']
            value = str(value)

    db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='ms0213',
                     db='project',
                     charset='utf8'
    )
    cursor = db.cursor()
    sql = f'''SELECT toilet.name, toilet.add, toilet.mb, toilet.ms, toilet.mhb, toilet.mhs, toilet.mcb, toilet.mcs, toilet.f, toilet.fh, toilet.fc FROM project.toilet where toilet.add like '%{value}%';'''

    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()


    return render_template("startbootstrap/result.html", result = result, num = len(result))

@app.route('/data', methods=['GET','POST'])
def data():

    db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='ms0213',
                     db='project',
                     charset='utf8'
    )
    cursor = db.cursor()
    sql = f'''SELECT toilet.name, toilet.add, toilet.mb, toilet.ms, toilet.mhb, toilet.mhs, toilet.mcb, toilet.mcs, toilet.f, toilet.fh, toilet.fc FROM project.toilet;'''

    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()


    return render_template("startbootstrap/data.html", result = result, num = len(result))



@app.route('/')
def home():
    
    return render_template("startbootstrap/home.html")


if __name__ == '__main__':
    app.run(debug=True)
