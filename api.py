from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from pymongo  import MongoClient
import json
from collection import Collection
from bson.objectid import ObjectId

# client = MongoClient(host="localhost", port=27017)
# db_uri = "mongodb+srv://Thomas:regliss22@cluster0.uc5d5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# client = MongoClient(db_uri)
app = Flask(__name__)
api = Api(app)

# def abort_if_todo_doesnt_exist(user_id):
#     if user_id not in users:
#         abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class User(Resource):
    # def get(self, user_id):
    #     abort_if_todo_doesnt_exist(user_id)
    #     return {"user_id": users[user_id]}

    def get(self, id):
        user = Collection.find_one({"_id": ObjectId(id)})
        return jsonify({
            'status': '200',
            'message': 'The request to get data has succeeded.',
            'data': str(user)
        })
    
    # def post(self):
    #     args = parser.parse_args()
    #     user_id = int(max(users.keys()).lstrip('user')) + 1
    #     user_id = 'user%i' % user_id
    #     users[user_id] = {'task': args['task']}
    #     return users[user_id], 201

    def post(self, id):
        if request.method == "POST":
            print(json.loads(request.data))
            user = json.loads(request.data)
            Collection.insert_one(user)
            return {
                'status': '200',
                'message': 'The user was created succsseffly.',
                'data': str(user)
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request',
                'data': [id]
            }


    # def put(self, user_id):
    #     # abort_if_todo_doesnt_exist(user_id)
    #     if request.method == "PUT":
    #         print(json.loads(request.data)["name"])
    #         users[user_id] = json.loads(request.data)["name"]
    #     return {user_id: users[user_id]}, 201

    def put(self, id):
        if request.method == "PUT":
            print(json.loads(request.data))
            user = json.loads(request.data)
            Collection.find_one_and_update(id)
            return {
                'status': 'ok',
                'message': 'The user was moldified succsseffly.',
                'data': [user]
            }
        else: 
            return {
                'status': '403',
                'message': 'Bad request',
                'data': [id]
            }


    def delete(self, id):
        return {
            'status': 'ok',
            'message': 'The user was deleted successfully.',
            'data': [id]
        }

api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)