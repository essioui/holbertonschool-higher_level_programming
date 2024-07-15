#!/usr/bin/python3

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    
    with open('items.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        items = data['items']
    
    
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
