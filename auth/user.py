import json
import uuid
from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256
from interpreter import db


class User:
    
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
        
    
    def register(self):
        
        request_json = json.loads(request.data)
        
        user = {
            "_id"     : uuid.uuid4().hex,
            "email"   : request_json["email"],
            "password": pbkdf2_sha256.encrypt(request_json["password"]),
            "pseudo"  : request_json["pseudo"]
        }
        
        # Check for existing email address
        if db.users.find_one({"email": user["email"]}):
            return jsonify({"error": "Email address already in use"}), 400
        
        if db.users.insert_one(user):
            return self.start_session(user)
    
    
        return jsonify({"error": "Signup failed"}), 400
    
    
    def signout(self):
        session.clear()