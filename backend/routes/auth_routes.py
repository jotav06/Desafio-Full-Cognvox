from flask import Blueprint
from controllers.auth_controller import home, login, dashboard, logout
from middlewares.auth_middleware import login_required

auth_bp = Blueprint('auth', __name__)

auth_bp.route("/")(home)
auth_bp.route("/login", methods=["POST"])(login)
auth_bp.route("/dashboard")(login_required(dashboard))
auth_bp.route("/logout")(logout)