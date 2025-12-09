from flask import Flask
from functions.routes import register_routes
import os

app = Flask(__name__, template_folder='views')
register_routes(app)

if __name__ == '__main__':
    app.run()
