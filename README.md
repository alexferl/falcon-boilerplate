# falcon-boilerplate [![Build Status](https://travis-ci.com/alexferl/falcon-boilerplate.svg?branch=master)](https://travis-ci.com/alexferl/falcon-boilerplate) [![codecov](https://codecov.io/gh/alexferl/falcon-boilerplate/branch/master/graph/badge.svg)](https://codecov.io/gh/alexferl/falcon-boilerplate)

A boilerplate for the [Falcon](https://github.com/falconry/falcon) framework.

## Requirements
- Python 3.7+
- [gunicorn](https://github.com/benoitc/gunicorn) as the WSGI HTTP server
- [meinheld](https://github.com/mopemope/meinheld) as the gunicorn worker
- [pydantic](https://github.com/samuelcolvin/pydantic) for data structures
- [vyper](https://github.com/alexferl/vyper) for config management
- [xid](https://github.com/alexferl/xid) for globally unique identifiers

## Using

```
$ git clone https://github.com/admiralobvious/falcon-boilerplate.git myapp
$ cd myapp
$ make dev
$ source venv/bin/activate
$ python run.py
```

To run the tests:

```
$ make test
```

## Optional Dependencies

- [fastjsonschema](https://github.com/horejsek/python-fastjsonschema) or
[jsonschema](https://github.com/Julian/jsonschema) if you wanna validate the requests/responses with
[JSON Schema](https://json-schema.org/). **NOTE**: The `/users` resources will not work if you don't have fastjsonschema or jsonschema installed.
- [falcon-crossorigin](https://github.com/admiralobvious/falcon-crossorigin) if you need
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) headers.
Must be enabled by passing `--cors-enabled` to `run.py` or any of the other ways supported by Vyper.
