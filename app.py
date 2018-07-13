from flask import Flask, render_template, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Products.db'
db = SQLAlchemy(app)


class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    origin = db.Column(db.Text)
    description = db.Column(db.Text)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)


    def __init__(self, pid, name, origin, description, quantity, unit_price):
        self.pid = pid
        self.name = name
        self.origin = origin
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def index_products():
    return render_template('index.html', rows=Products.query.all())


@app.route('/products/<int:pid>')
def product_details(pid):
    return render_template('details.html', p=Products.query.filter_by(ProductID=pid).one())


if __name__ == '__main__':
    db.create_all()
    db.session.add_all(1, 'Apple', 'Hong Kong', 'Big red apple', 100, 5)
    db.session.add_all(2, 'Banana', 'London', 'Yellow Banana', 1000, 5)
    app.run(debug=True, host="0.0.0.0", port=8000)
