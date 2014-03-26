# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from api import app
from flask import jsonify as JSON
from cors import cors


@app.route('/')
@cors(origin='*')
def index():
    return JSON(welcome='Welcome to Liv API')


@app.route('/status')
@cors(origin='*')
def status():
    return JSON(apiStatus=True, storageStatus=True)
