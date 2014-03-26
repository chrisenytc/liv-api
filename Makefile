# liv-api
# https://github.com/chrisenytc/liv-api
#
# Copyright (c) 2014 Christopher EnyTC
# Licensed under the MIT license.


install:
	pip install -r requirements.txt

start:
	@PY_ENV=production python runserver.py

test:
	@PY_ENV=test python test/test_liv-api.py

.PHONY: install test