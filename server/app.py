#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
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

    return make_response([b.to_dict() for b in Bakery.query.all()], 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    
    bakery = Bakery.query.filter(Bakery.id == id).first()
    
    return make_response(bakery.to_dict(), 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    goods_by_price = [bg.to_dict() for bg in BakedGood.query.order_by(BakedGood.price).all()]

    return make_response(goods_by_price, 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():

    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first().to_dict()

    response = make_response(most_expensive,200)

    return response

if __name__ == '__main__':
    app.run(port=555, debug=True)
