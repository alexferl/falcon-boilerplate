# falcon-boilerplate [![Build Status](https://travis-ci.org/admiralobvious/falcon-boilerplate.svg?branch=master)](https://travis-ci.org/admiralobvious/falcon-boilerplate)

A Python 3 boilerplate for the [Falcon](https://github.com/falconry/falcon) framework. Uses [gunicorn](https://github.com/benoitc/gunicorn) as the WSGI HTTP server and [meinheld](https://github.com/mopemope/meinheld) as the gunicorn worker. It also uses [Vyper](https://github.com/admiralobvious/vyper) for [12-factor](https://12factor.net/).

## Using

```
$ git clone https://github.com/admiralobvious/falcon-boilerplate.git
$ mv falcon-boilerplate your_app
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r dev_requirements.txt
$ python run.py
```

To run the tests:

```
$ nose2 tests
```
