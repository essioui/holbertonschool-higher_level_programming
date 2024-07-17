#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
        return []


@app.route('/products')
def products():
    
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)


    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source."), 400

    products = []


    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')


    if product_id is not None:
        products = [product for product in products if int(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found."), 404

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
