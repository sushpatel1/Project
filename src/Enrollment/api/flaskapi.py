from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
from Enrollment.adapters.orm import start_mappers, metadata
from Enrollment.domain import commands
from Enrollment.api import views
from Enrollment import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()

@app.route('/')
def index(self):
    return f'Enrollment API'

  
@app.route('/add_member', methods=['POST'])
def add_member():
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    age = request.json["age"]
    gender = request.json["gender"]
    active = request.json["active"]
    date_added = request.json["date_added"]
    date_edited = request.json["date_edited"]

    cmd = commands.AddMemberCommand(
            first_name, last_name, age,gender,active, date_added, date_edited
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/members/<first_name>", methods=['GET'])
def get_member_by_firstname(self, first_name):
    result = views.members_view(first_name, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

def delete(self, bookmark):
    pass

def update(self, bookmark):
    pass

if __name__ == "__main__":
    app.run()