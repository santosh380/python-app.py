from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management API"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({user_id: user})

# POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User added", "user": {user_id: data}}), 201

# PUT - Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users[user_id] = data
    return jsonify({"message": "User updated", "user": {user_id: data}})

# DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
