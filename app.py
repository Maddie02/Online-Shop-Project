import json

from flask import Flask
from flask import request
from flask import render_template

from model.user import User
from model.ad import Ad

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def shop():
    return render_template("index.html")

@app.route("/users", methods = ["POST"])
def create_user():
    user_data = request.get_json(force=True, silent=True)
    if user_data == None:
        return "Bad request", 400
    user = User(user_data["id"], user_data["email"], user_data["password"], user_data["name"], user_data["address"], user_data["phone_number"]) 
    user.save()
    return json.dumps(user.to_dict()), 201


@app.route("/users/<int:id>", methods = ["GET"])
def find_user(id):
    return json.dumps(User.find_by_id(id).to_dict())

@app.route("/users/<name>", methods = ["GET"])
def find_by_username(name):
    return json.dumps(User.find_by_name(name).to_dict())

@app.route("/users", methods = ["GET"])
def get_all_users():
    all_users = {"all": []}
    for user in User.get_all():
        all_users["all"].append(user.to_dict())
    return json.dumps(all_users)


@app.route("/users/<int:id>", methods = ["PATCH"])
def change_user_info(id):
    user_data = request.get_json(force=True, silent=True)
    if user_data == None:
        return "Bad request", 400

    user = User.find_by_id(id)

    if "name" in user_data:
        user.name = user_data["name"]
    
    if "address" in user_data:
        user.address = user_data["address"]

    if "phone_number" in user_data:
        user.phone_number = user_data["phone_number"]
    
    return json.dumps(user.save().to_dict())


@app.route("/users/<int:id>", methods = ["DELETE"])
def delete_user(id):
    User.delete(id)
    return "" 
          
          
if __name__ == "__main__":
    app.run()

