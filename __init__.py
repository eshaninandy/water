from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

@app.route('/') #for login
def student():
   return render_template('student1.html')

@app.route('/made') #for new user
def made():
   return render_template('register.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    state=-1
    conn = sqlite3.connect('main.sqlite')
    cur = conn.cursor()
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('SELECT * FROM clinic WHERE name = ? and pass = ?', (result['Name'],result['password'],))
      try:
        state=int(cur.fetchone()[0])
      except:
        return render_template('student1.html', seto=1)
    return render_template("result.html",result = result)




@app.route('/create',methods = ['POST', 'GET'])
def create():
    state=-1
    conn = sqlite3.connect('main.sqlite')
    cur = conn.cursor()
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('''INSERT OR IGNORE INTO clinic (uid,name,pass)VALUES ( ?,?, ?)''', ( random.randint(0,5000),result['Name'],result['password'], ))
      conn.commit()    
      return render_template("result.html",result = result)
    return "hi"

if __name__ == '__main__':
   app.run(debug = True) 