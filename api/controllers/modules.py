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
from auth import require_auth


@app.route('/modules')
@cors(origin='*')
@require_auth(roles='*')
def modules_index():
    modules_data = User.objects(email=request.user['email']).get()['modules']
    return JSON(modules=modules_data, total=len(modules_data))


@app.route('/modules', methods=['PUT'])
@cors(origin='*', methods=['PUT'])
@require_auth(roles='*')
def modules_update():
    modules = User.objects(email=request.user['email'])
    modules.update(set__modules=request.get_json()['modules'])
    return JSON(message='Modules updated successfully!')
