#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
        
@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    
    return make_response(
        [bakery.to_dict() for bakery in Bakery.query.all()],
        200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    return make_response(
        Bakery.query.filter(Bakery.id == id).first().to_dict(),
        200
    )

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    return make_response(
        [baked_good.to_dict() for baked_good in  BakedGood.query.order_by(BakedGood.price.desc()).all()],
        200
    )

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return make_response(
        BakedGood.query.order_by(BakedGood.price.desc()).first().to_dict(),
        200
    )

if __name__ == '__main__':
    app.run(port=5555, debug=True)
