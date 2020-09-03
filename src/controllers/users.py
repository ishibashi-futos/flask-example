from flask import Blueprint, request
from flask_restful import Resource, Api

users = []

app = Blueprint('users', __name__)
api = Api(app)

class UsersController(Resource):
  def get(self):
    name = request.args.get("name")
    print(name)
    if name == None:
      user = list(filter(lambda n: n["name"] == name, users))
      if len(user) == 0:
        return {"users": []}
      return {"users": users}
    else :
      return {"users": users}
  def post(self):
    json = request.get_json(force = True)
    print(json)
    users.append({"name": json["name"]})
    return json

api.add_resource(UsersController, '/users')
