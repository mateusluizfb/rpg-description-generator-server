import settings
from flask import Flask
from lib.twitter_client import TwitterClient
import lib.scheduler

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"
