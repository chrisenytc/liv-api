# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from functools import wraps
from flask import request, abort
from api import app
from api.models.user import User


def require_auth(roles=''):
    def auth_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            access_token = request.args.get('access_token', '')
            user_info = User.objects(token=access_token)
            if app.config['AUTH']['enabled']:
                if user_info.count() is 0 or user_info.get().status is False:
                    abort(401)
                else:
                    user_data = dict(
                        id=str(user_info.get().id),
                        name=user_info.get().name,
                        email=user_info.get().email,
                        password=user_info.get().password,
                        roles=user_info.get().roles,
                        token=user_info.get().token,
                        status=user_info.get().status)
                    if roles != '*':
                        if any(value in user_info.get().roles
                               for value in roles):
                            request.user = user_data
                            request.profile = user_info.get()
                            return function(*args, **kwargs)
                        else:
                            abort(401)
                    else:
                        request.user = user_data
                        request.profile = user_info.get()
                        return function(*args, **kwargs)
            else:
                return function(*args, **kwargs)
        return wrapper
    return auth_decorator
