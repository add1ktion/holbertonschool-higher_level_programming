#!/usr/bin/python3
"""Simple Flask API with user management endpoints."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Serve the API welcome message."""
    return "Welcome to the Flask API!\n"


@app.route("/data")
def data():
    """Return a JSON list of all usernames."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    """Return API status."""
    return "OK\n"


@app.route("/users/<username>")
def show_user_profile(username):
    """Get user by username or 404."""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """POST new user or error 400/409."""
    try:
        user_data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if 'username' not in users_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify(user_data), 201


if __name__ == "__main__":
    app.run()
