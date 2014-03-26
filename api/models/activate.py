# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from mongoengine import *


class Activate(Document):
    email = StringField(required=True, unique=True)
    token = StringField(required=True, unique=True)
