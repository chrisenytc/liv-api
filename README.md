# Liv API [![Build Status](https://secure.travis-ci.org/chrisenytc/liv-api.png?branch=master)](http://travis-ci.org/chrisenytc/liv-api) [![GH version](https://badge-me.herokuapp.com/api/gh/chrisenytc/liv-api.png)](http://badges.enytc.com/for/gh/chrisenytc/liv-api) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/chrisenytc/liv-api/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

> A API for Liv

## Getting Started

1º Clone liv-api repo

```bash
git clone https://github.com/chrisenytc/liv-api.git
```

2º Enter in liv-api directory
```bash
cd liv-api
```

3º Install dependencies

if you no have virtualenv installed. Install it.

```bash
sudo apt-get install python-virtualenv
```

```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

```bash
make install
```

4º Configure the settings in `api/config`

5º Run liv-api

```bash
make start
```

Test your liv-api

```bash
make test
```

## Contributing

See the [CONTRIBUTING Guidelines](CONTRIBUTING.md)

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/chrisenytc/liv-api/issues).

## License

Copyright (c) 2014 Christopher EnyTC

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.