#!/usr/bin/python3
"""A Flask web application that renders an HTML template with logic to display items from a JSON file."""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
        return render_template('items.html', items=data['items'])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        items = []
        return render_template('items.html', items=items)
    
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        product_id = int(product_id)

    try:
        if source == 'json':
            with open('products.json') as f:
                data = json.load(f)
                products = data
        elif source == 'csv':
            with open('products.csv', newline='') as f:
                reader = csv.DictReader(f)
                products = list(reader)
        if product_id:
            products = [p for p in products if str(p.get('id')) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)
    except FileNotFoundError:
        return render_template('product_display.html', error="Product not found")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
