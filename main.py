from flask import Flask, session, render_template, redirect, url_for, request, flash
import sqlite3
app = Flask('app')
app.debug = True
app.secret_key = "CHANGE ME"

@app.route('/', methods=['GET', 'POST'])
def login():
  error = "Create Account?"
  login = "Successfully logged in!"
  # If the username/password is correct, log them in and redirect them to the home page.
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  
  if request.method == 'POST':
    session['user'] = request.form["username"]
    session['pw'] = request.form["password"]
    cursor.execute("SELECT password FROM users WHERE username = ?", (session['user'],))
    values = cursor.fetchone()
    #print(values)
    connection.commit()
    connection.close()
    login = "Successful"

    if values is None or session['pw'] != values[0]:
      error = "Username or password does not exist. Create account?" #LINK TO THE DEF CREATEACCOUNT METHOD
      return render_template("login.html", error = error, values = values)
    elif session['pw'] == values[0]:
      return redirect('/home')

  return render_template("login.html", error = error)

#
@app.route('/logout', methods=['GET', 'POST'])
def logout():
  # Log the user out and redirect them to the login page
  session.pop('user', None)
  session.pop('pw', None)
  session.pop('user_type', None)
  session.pop('cart', None)
  session.pop('q', None) 
  session.clear()
  return redirect('/')

@app.route('/createaccount', methods=['GET', 'POST'])
def create():
  message = ""
  if request.method == 'POST':
    name = request.form["name"]
    user = request.form["username"]
    pw = request.form["password"]
    email = request.form["email"]

    connection = sqlite3.connect("myDatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
    values = cursor.fetchall()
    print("DEBUG: " + str(values))
    print(values)
    if len(values) == 0:
      cursor.execute("INSERT INTO users (username, password, name, email) VALUES (?,?,?, ?)", (user, pw, name, email))
      message = "Account created! Please return to the login page"
    else:
      message = "Username already exists. Please try again."
    connection.commit()
    connection.close()
  return render_template('accountCreation.html', message = message)

@app.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM users WHERE username = ?", (session['user'],))
  values = cursor.fetchone()
  #print("DEBUG " + values)
  connection.commit()
  connection.close()

  return render_template('userinfo.html', values = values)


#BASICALLY FIX ALL OF THIS TO DISPLAY THE ITEMS IN THE DATABASE
@app.route('/home', methods=['GET', 'POST'])
def home():
  login = "Not logged in"
  if 'user' in session:
    login = "Successfully logged in."
    session['cart'] = {'Your items': "quantity"}

  if request.method == 'POST':
    session['search'] = request.form['search']    
    return redirect('/search')
    '''connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    search = request.form['search']
    print(search)
    cursor.execute("SELECT * FROM items WHERE name LIKE ? OR name LIKE ?", (('%' + search), (search + '%'),))
    values=cursor.fetchall() 
    print(values)
    connection.commit()
    connection.close()
    return render_template("All.html", values = values)'''
    #cursor.execute("SELECT * FROM users WHERE username = ?" (session['user']))
  return render_template("home.html", login = login)#, values = values), students = values, user = session['name'])


@app.route('/ProteinBars', methods=['GET', 'POST'])
def ProteinBars():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM items WHERE type = ? ", ("Protein Bar",),)
  values=cursor.fetchall() 
  connection.commit()
  connection.close()
  return render_template("All.html", values = values)

@app.route('/ProteinShakes')
def ProteinShakes():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM items WHERE type = ? ", ("Protein Shake",),)
  values=cursor.fetchall() 
  connection.commit()
  connection.close()
  return render_template("All.html", values = values)
 # return render_template("ProteinShakes.html")

@app.route('/Creatine')
def Creatine():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM items WHERE type = ? ", ("Creatine",),)
  values=cursor.fetchall() 
  connection.commit()
  connection.close()
  return render_template("All.html", values = values)

@app.route('/Caffeine')
def Caffeine():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM items WHERE type = ? ", ("Caffeine",),)
  values=cursor.fetchall() 
  connection.commit()
  connection.close()
  return render_template("All.html", values = values)

@app.route('/All', methods=['GET', 'POST'])
def All():
  if request.method == 'POST':
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    itemid = request.form['prod']
    quantity = request.form['quantity']
    session['q'] = request.form['quantity']

    
    session['cart'][itemid] = quantity
    session.modified = True

  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM items")
  values=cursor.fetchall() 


  connection.commit()
  connection.close()

  return render_template('All.html', values = values)
  #return render_template("All.html")

@app.route('/checkout')
def checkout():
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  
  keys = session['cart'].keys()
  if keys is None:
    return redirect('/logout')
  else:
    q = session['q']
    #for k in range(len(list(keys))):
    i = 0
    for k in list(keys):
      cursor.execute("UPDATE items SET stock = stock - ? WHERE id = ? ", (session['cart'][k], list(keys)[i],))
      i+=1
  values=cursor.fetchall()    
  connection.commit()
  connection.close()
  return redirect('/logout')

@app.route('/search')
def search():
  #TODO:
  #if request.method == 'POST':
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  search = session['search']
  cursor.execute("SELECT * FROM items WHERE name LIKE ? OR name LIKE ?", (('%' + search), (search + '%'),))
  session.pop('search', None)
  values=cursor.fetchall() 

  connection.commit()
  connection.close()
  return render_template("All.html", values = values)

@app.route('/Cart', methods = ['GET', 'POST'])
def Cart():

  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()

  session.modified = True
  keys = session['cart'].keys()
  if keys is None:
    cursor.execute("SELECT * FROM items")
  else:
    cursor.execute("SELECT * FROM items WHERE id IN (?)", (list(keys)[0],))
  values=cursor.fetchall()    
  connection.commit()
  connection.close()



  return render_template("Cart.html", values = values, keys = keys)



app.run(host='0.0.0.0', port=8080)
