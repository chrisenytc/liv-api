# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import os


class Development():
    API = {
        'name': 'Liv - Development',
        'description': 'A API for Liv',
        'version': 'v1',
        'debug': True,
        'documentation_url': 'https://github.com/chrisenytc/liv#documentation'
    }
    AUTH = {
        'enabled': True
    }
    MAIL = {
        'email': os.environ.get('MAIL_EMAIL', ''),
        'password': os.environ.get('MAIL_PASSWORD', '')
    }
    DATABASE = {
        'uri': 'mongodb://localhost/liv'
    }
    ERRORS = {
        '500': 'Internal Server Error',
        '503': 'Service Unavailable',
        '400': 'Bad Request',
        '401': 'Bad Authentication. You do not have permission to access the API',
        '404': 'Not Found'
    }
