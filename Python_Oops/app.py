#CRUD APPLICATION - CREATE READ UPDATE DELETE

# emailfromsql
# if email==emailfromsql:
#     msg = "login succesful"
# else:
#     msg="invalid mail"
    
# app.route('/login')
# def login():
#     select username,pwd 
#     selected username == entered username : login success! -> homepage of fb


# @app.route('/register')
# def register():
#     "insert into....."

# select * from table where username='ss'


#account = {'username':'Sanjana','password':'pwd',.......}

from flask import Flask,render_template,url_for,request,session,redirect

from flask_mysqldb import MySQL

import MySQLdb.cursors #is used for executing stmts


app = Flask(__name__)

app.secret_key = "my secret key"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1328'
app.config['MYSQL_DB'] = 'crude_app'
#
mysql = MySQL(app)
'''
<li><a href="{{url_for('update')}}">Update</a></li>
					<li><a href="{{url_for('logout')}}">Log out</a></li>
	<ul>
					<li class="active"><a href="{{url_for('index')}}">Index</a></li>
					<li><a href="{{url_for('display')}}">Display</a></li>
					<li><a href="{{url_for('update')}}">Update</a></li>
					<li><a href="{{url_for('logout')}}">Log out</a></li>
				</ul>
'''
@app.route('/')
@app.route('/login',methods=['GET','POST'])
def login():
    msg = ''
    if request.method== 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        pwd = request.form['password']
        
        mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mycursor.execute("SELECT * FROM accounts WHERE username = %s AND password=%s",(username,pwd))
        account = mycursor.fetchone()
        # account = {id:1,username:'Sanjana',email:'sen',......}
        
        if account:
            msg = 'Login Succesfull!'
            
            #make my session active
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            
            #session = {loggedin:True,id:1,username:Sanjana}
            
            return render_template('index.html',msg = msg)
        
        else:
            msg = "Incorrect username/password "
    
    return render_template('login.html',msg = msg)


@app.route('/logout')
def logout():
    #pop() - this is used to remove elements from a lisst/dictionary
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    
    return redirect(url_for('login'))

 
@app.route('/register',methods=['POST','GET'])
def register():
    msg = ''
    if request.method== 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'organisation' in request.form and 'address' in  request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form:
        
        username = request.form['username']
        pwd = request.form['password']
        email= request.form['email']
        org = request.form['organisation']
        add = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        postal = request.form['postalcode']
        
        mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mycursor.execute('SELECT * FROM ACCOUNTS WHERE username = %s',(username,))
        account = mycursor.fetchone() #fetchone func is used to retrieve only 1 record,if u want to fetch all records, fetchall()
        
        # account = {id:1,username:'Sanjana',email:'sen',......} , {} - if the account does not exist, this is how the dict is gooing to be
        if account:
            msg = 'Account Already Exists!'
        
        else:
            mycursor.execute("INSERT INTO accounts VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(username,pwd,email,org,add,city,state,country,postal))
            mysql.connection.commit()
            
            msg = "Registration Successfull!"
    
    elif request.method=='POST':
        msg = 'Fill out the form completely!'
        
        
    return render_template('register.html',msg = msg)

@app.route('/index')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    return render_template('login.html')

@app.route('/display')
def display():
    if 'loggedin' in session:
        mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        mycursor.execute('SELECT * FROM accounts where id=%s',(session['id'],))
        account = mycursor.fetchone()
        
        return render_template('display.html',account=account) #return = stop

    
    return render_template('login.html')


@app.route('/update',methods=['POST','GET'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method== 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'organisation' in request.form and 'address' in  request.form and 'city' in request.form and 'state' in request.form and 'country' in request.form and 'postalcode' in request.form:
        
            username = request.form['username']
            pwd = request.form['password']
            email= request.form['email']
            org = request.form['organisation']
            add = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            postal = request.form['postalcode']
            
            mycursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            mycursor.execute('UPDATE accounts set username = %s,password=%s,email=%s,organisation=%s,address=%s,city=%s,state=%s,country=%s,postalcode=%s where id=%s',(username,pwd,email,org,add,city,state,country,postal,session['id']))
            mysql.connection.commit()
            
            msg = "Updated Successfully!"
            
        elif request.method == 'POST':
            msg = "Fill out completely!"
            
        return render_template('update.html',msg=msg)
    
    return render_template('login.html')
            
            
            
        
        
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
        
    
        
        
        
        
        
        

# @app.route('\register')
# def reg():
#     insert into
#     reg successfull

  
  
#   MAINTENANCE!!!!!!!!
#   SFTW QUALITY ASSURANCE
  