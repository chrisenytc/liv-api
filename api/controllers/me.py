# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from api import app
from flask import request
from flask import jsonify as JSON
from api.models.user import User
from cors import cors
from hashlib import sha1
from auth import require_auth


@app.route('/me')
@cors(origin='*')
@require_auth(roles='*')
def me_index():
    request.user.pop('password', None)
    request.user.pop('modules', None)
    return JSON(request.user)


@app.route('/me', methods=['PUT'])
@cors(origin='*', methods=['PUT'])
@require_auth(roles='*')
def me_update():
    data = request.get_json()
    user = User.objects(email=request.user['email'])
    if data['name'] != '':
        user.update(set__name=data['name'])
    if data['email'] != '':
        user.update(set__email=data['email'])
    if data['password'] != '':
        user.update(set__password=sha1(data['password']).hexdigest())
    return JSON(message='Account updated successfully!')


@app.route('/me', methods=['DELETE'])
@cors(origin='*', methods=['DELETE'])
@require_auth(roles='*')
def me_delete():
    user = User.objects(email=request.user['email'])
    user.delete()
    return JSON(message='Account deleted successfully!')
