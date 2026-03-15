from flask import Flask
from flask_cors import CORS
import os
from database import create_database, create_tables, create_initial_user

from routes.auth_routes import auth_bp

template_dir = os.path.abspath('../frontend/templates')
static_dir = os.path.abspath('../frontend/static')

app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

CORS(app)

create_database()
create_tables()
create_initial_user()

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
    