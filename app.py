from flask import Flask
from config import *

app = Flask(__name__)

greetings = "Production greetings"

try:
    from instance import windows_development_configuration
    app.config.from_object(DevelopmentConfig)
    greetings = windows_development_configuration.greetings
except:
    app.config.from_object(ProductionConfig)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello mobilemate, from "+greetings

if __name__ == '__main__':
    app.run()