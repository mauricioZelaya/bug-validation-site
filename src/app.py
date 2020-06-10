from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add-user')
def add_user():
    return render_template('add-user.html')


@app.route('/edit-users')
def edit_users():
    return render_template('edit-users.html')


@app.route('/delete-user')
def delete_user():
    return render_template('delete-user.html')


if __name__ == '__main__':
    app.run(debug=True)

