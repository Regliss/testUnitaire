from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
import json
from collection import User_Collection
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# def abort_if_todo_doesnt_exist(user_id):
#     if user_id not in users:
#         abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class User(Resource):

    def get(self, id):
        if request.method == "POST":
            user = User_Collection.find_one({"_id": ObjectId(id)})
            return jsonify({
                'status': '200',
                'message': 'The request to get data has succeeded.',
                'data': str(user)
            })
        else:
            return jsonify({
                'status': '403',
                'message': 'Bad request',
                'data': str(id)
            })

    def post(self, id):
        if request.method == "POST":
            print(json.loads(request.data))
            user = json.loads(request.data)
            User_Collection.insert_one(user)
            return {
                'status': '200',
                'message': 'The user was created succsseffly.',
                'data': str(user)
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request',
                'data': str(id)
            }

    def put(self, id):
        if request.method == "PUT":
            print(json.loads(request.data))
            user = json.loads(request.data)
            User_Collection.find_one_and_update({"_id":ObjectId(id)}, {"$set" : user}, upsert = True);
            return {
                'status': 'ok',
                'message': 'The user was moldified succsseffly.',
                'data': [user]
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request',
                'data': str(id)
            }


    def delete(self, id):
        if request.method == "DELETE":
            return {
                'status': '200',
                'message': 'The user was deleted successfully.',
                'data': str(id)
            }
        else:
            return {
                'status': '403',
                'message': 'Bad Request',
                'data': str(id)
            }

api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)