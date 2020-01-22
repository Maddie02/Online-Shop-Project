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
    all_users = {"All users": []}
    for user in User.get_all():
        all_users["All users"].append(user.to_dict())
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

@app.route("/ads", methods = ["POST"])
def create_ad():
    ad_data = request.get_json(force=True, silent=True)
    if ad_data == None:
        print(ad_data)
        return "Bad request", 400
    ad = Ad(ad_data["id"], ad_data["title"], ad_data["description"], ad_data["price"], ad_data["date"], ad_data["is_active"], ad_data["owner_id"]) 
    ad.save()
    return json.dumps(ad.to_dict()), 201

@app.route("/ads", methods = ["GET"])
def get_all_ads():
    all_ads = {"All ads": []}
    for ad in Ad.get_all():
        all_ads["All ads"].append(ad.to_dict())
    return json.dumps(all_ads)

@app.route("/ads/<id>", methods = ["GET"])
def find_ad(id):
    return json.dumps(Ad.find_by_id(id).to_dict())

@app.route("/ads/<id>", methods = ["PATCH"])
def change_ad_info(id):
    ad_data = request.get_json(force=True, silent=True)
    if ad_data == None:
        return "Bad request", 400

    ad = Ad.find_by_id(id)

    if "title" in ad_data:
        ad.title = ad_data["title"]
    
    if "description" in ad_data:
        ad.description = ad_data["description"]

    if "price" in ad_data:
        ad.price = ad_data["price"]
    
    if "date" in ad_data:
        ad.date = ad_data["date"]
    
    return json.dumps(ad.save().to_dict())


if __name__ == "__main__":
    app.run()

