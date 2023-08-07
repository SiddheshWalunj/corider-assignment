from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import user_auth

app = Flask(__name__)

app.config['MONGODB_URI'] = 'mongodb://localhost:27017/corider'
app.config['MONGODB_DATABASE'] = 'corider'

db = MongoClient(app.config['MONGODB_URI'])[app.config['MONGODB_DATABASE']]

@app.route('/all_users', methods=['GET'])
def get_all_user():
    users = db.user_data.find()
    user_list = []
    for user in users:
        user_dict = {
            '_id':str(user['_id']),
            'name':user['name'],
            'email':user['email']
        }
        user_list.append(user_dict)
    return jsonify(user_list)


@app.route('/get_users/<id>',methods=['GET'])
def get_user(id):
    user = db.user_data.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify({'_id': str(user['_id']), 'name': user['name'], 'email': user['email']})
    else:
        return jsonify({'message': 'User not found.'}), 404


@app.route('/add_users', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    if not name:
        return {"status": "false", "message":"please provide the user name"}
    
    if not email:
        return {"status": "false", "message":"please provide the email id"}
    
    if not password:
        return {"status":"false", "message":"please enter password"}
    
    result = user_auth.register_user(db, name, email, password)
    return jsonify(result)

@app.route('/update_user/<id>',methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    result = db.user_data.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email, 'password': password}})

    if result.matched_count > 0:
        return {"status" : "true", "message":"User Updated Successfully"}
    else:
        return {"status" : "false", "message":"User not found"}


@app.route('/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    result = db.user_data.delete_one({'_id': ObjectId(id)})

    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted successfully.'})
    else:
        return jsonify({'message': 'User not found.'}), 404


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
