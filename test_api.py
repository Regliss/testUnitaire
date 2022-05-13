import requests

# Test Create
Create = requests.post("http://127.0.0.1:5000/create", json={"nom":"Thomas2", "age": 24}).status_code
if Create == 200:
    print("le Create marche")
else:
     print("le Create ne marche pas")
 
# Test Get
Get = requests.get("http://127.0.0.1:5000/user/Thomas2").status_code
if Get == 200:
    print("le Get marche")
else:
    print("le Get ne marche pas")

# Test Put
Put = requests.put("http://127.0.0.1:5000/update/Thomas2", json={"nom":"Thomas3", "age": 24}).status_code
if Put == 200:
    print("le Put marche")
else:
    print("le Put ne marche pas")

# Test GetAll
GetAll = requests.get("http://127.0.0.1:5000/users").status_code
if GetAll == 200:
    print("le GetAll marche")
else:
    print("le GetAll ne marche pas")