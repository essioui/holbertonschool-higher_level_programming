#!/usr/bin/python3
"""Define"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpassword"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"msg": "Invalid username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"msg": "Basic Auth: Access Granted"}), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"msg": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    else:
        return jsonify({"msg": "Admin Access: Granted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
