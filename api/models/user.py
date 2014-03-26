# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from mongoengine import *


class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    roles = ListField(default=['user'])
    token = StringField(required=True, unique=True)
    status = BooleanField(default=False)
    modules = ListField(default=[])

    def clean(self):
        if User.objects(email=self.email).count():
            msg = 'This email already exists!'
            raise ValidationError(msg)
