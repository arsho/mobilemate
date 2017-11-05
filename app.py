from flask import Flask
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello mobilemate"

if __name__ == '__main__':
    app.run()