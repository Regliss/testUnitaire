from flask import Flask, jsonify, request

app = Flask(__name__)
users = [
    {
        'nom': 'Thomas',
        'age': 23
    }
]


@app.route('/')
def home():
    return jsonify(users)


@app.route('/create', methods=['POST'])
def create():
    request_data = request.get_json()
    new_user = {
        'nom': request_data['nom'],
        'age': request_data['age'],
    }
    users.append(new_user)
    return jsonify(new_user)

@app.route('/update/<string:nom>', methods=['PUT'])
def update(nom):
    request_data = request.get_json()
    for user in users:
        if(user['nom'] == nom):
            user['nom'] = request_data['nom']
            user['age'] = request_data['age']
            return jsonify({'message': 'succes'})
    return jsonify({'message': 'user not found'})


@app.route('/user/<string:nom>')
def get(nom):
    for user in users:
        if(user['nom'] == nom):
            return jsonify({'age': user['age']})
    return jsonify({'message': 'user not found'})


@app.route('/users')
def getAll():
    return jsonify({'users': users})

app.run(port=5000)