from flask import Flask, render_template, request, flash
from flask_session import Session
from flask_mysqldb import MySQL

app = Flask(__name__)
sess = Session()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Control123!'
app.config['MYSQL_DB'] = 'agenda'
mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO usuario (usr_first_name, usr_last_name, usr_phone_nbr, usr_email) '
                       'VALUES (%s, %s, %s, %s);', (first_name, last_name, phone, email))
        mysql.connection.commit()
        flash("contacto agregado satisfactoriamente!!!")

    return render_template('add-user.html')


@app.route('/edit-users')
def edit_users():
    return render_template('edit-users.html')


@app.route('/delete-user')
def delete_user():
    return render_template('delete-user.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_USE_SIGNER'] = False
    app.config['SESSION_PERMANENT'] = True

    sess.init_app(app)

    app.run(debug=True)

