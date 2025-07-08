from flask import Flask
from views import register_views
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "d3c2d4f4aef8cf6bc0e0f35e214d87fcd4719e593a2e4d0f96a7635029c3d294"

register_views(app)

if __name__ == '__main__':
    app.run(debug=True,port=8000, host='0.0.0.0')
