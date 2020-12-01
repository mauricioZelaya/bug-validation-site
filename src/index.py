from flask import Flask, render_template, request, flash, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import redirect
from werkzeug.utils import redirect

app = Flask(__name__)

ENV = 'dev'

sess = Session()
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_USE_SIGNER'] = False
app.config['SESSION_PERMANENT'] = True

sess.init_app(app)

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Control123!@localhost/'

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pkmeechmeklwey:19cf0fc346c52c704cfcdfa855e543696951cf848a8db9146f089e769e0e6afa@ec2-52-87-135-240.compute-1.amazonaws.com:5432/d5l0uqffiart14'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class usuario(db.Model):
    __tablename__ = 'usuario'
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_first_name = db.Column(db.String(200))
    usr_last_name = db.Column(db.String(200))
    usr_password = db.Column(db.String(200))
    usr_phone_nbr = db.Column(db.String(200))
    usr_email = db.Column(db.String(200))

    print("table created successfully")

    def __init__(self, usr_first_name, usr_last_name, usr_password, usr_phone_nbr, usr_email):
        self.usr_first_name = usr_first_name
        self.usr_last_name = usr_last_name
        self.usr_password = usr_password
        self.usr_phone_nbr = usr_phone_nbr
        self.usr_email = usr_email


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

        data = usuario(first_name, last_name, password, phone, email)

        db.session.add(data)
        db.session.commit()

        flash("contacto agregado satisfactoriamente!!!")

    return render_template('add-user.html')


@app.route('/list-users')
def list_users():
    rows = db.session.query(usuario).all()
    # print(rows)
    for row in rows:
        print(row.usr_first_name)
    return render_template('list-users.html', contacts=rows)


@app.route('/edit-users')
def edit_users():
    rows = db.session.query(usuario).all()
    # print(rows)
    for row in rows:
        print(row.usr_first_name)
    return render_template('edit-user.html', contacts=rows)


@app.route('/delete-user')
def delete_user():
    rows = db.session.query(usuario).all()
    # print(rows)
    for row in rows:
        print(row.usr_first_name)
    return render_template('delete-user.html', contacts=rows)


@app.route('/delete/<string:usr_id>')
def delete_contact(usr_id):

    data = usuario.query.get(usr_id)
    print(data)
    db.session.delete(data)
    db.session.commit()
    flash('contact deleted successfully')
    return redirect(url_for("delete_user"))

if __name__ == '__main__':

    app.run()

