from flask import Flask
import pymongo


app = Flask(__name__)
app.secret_key = b'T\xee\xc2\xc3&\xb2\xd5\x8e;\xe9\xe4B\xdc?\xbe)'


# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

# Routes
from auth import routes

@app.route('/')
def home():
    return "Home"