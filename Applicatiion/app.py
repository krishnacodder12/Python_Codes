from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Replace these values with your MySQL database credentials
db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, password))
    db.commit()
    cursor.close()

    return "Account Registered"

if __name__ == '__main__':
    app.run(debug=True)
