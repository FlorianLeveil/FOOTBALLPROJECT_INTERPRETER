from flask import Flask
from interpreter import app
from auth.user import User


@app.route('/user/register', methods=['POST'])
def register():
    return User().register()
