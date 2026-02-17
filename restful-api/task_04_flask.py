#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!\n"

@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    return "OK\n"

@app.route("/users/<username>")
def show_user_profile(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user")
def add_user():
    try:
        user_data = request.get_json()
    except:
        jsonify({"error": "Invalid JSON"}), 400
    
    if 'username' not in users_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']

    if username in user_data:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify(user_data), 201

if __name__ == "__main__": app.run()