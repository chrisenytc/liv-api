#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import os
import newrelic.agent
from api import app

# Start new relic
newrelic.agent.initialize('newrelic.ini')

# Start Liv
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 22792))
    app.run('0.0.0.0', port=port)
