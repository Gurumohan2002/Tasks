from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success')
def success():
   return 'welcome %s'  

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == ['GET','POST']:
      user = request.form['nm']
      return redirect(url_for('success'))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__ == '__main__':
   app.run(debug = True)