from functools import wraps
from flask import request, redirect, url_for, make_response
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        token = request.cookies.get("access_token")

        if not token:
            return redirect(url_for("auth.home"))

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):

            resp = make_response(redirect(url_for("auth.home")))
            resp.delete_cookie("access_token")

            return resp

        return func(*args, **kwargs)

    return wrapper