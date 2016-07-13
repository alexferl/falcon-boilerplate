# falcon-boilerplate

A simple boilerplate for the [Falcon](https://github.com/falconry/falcon) framework. Uses [gunicorn](https://github.com/benoitc/gunicorn) as the WSGI HTTP server and [meinheld](https://github.com/mopemope/meinheld) as the gunicorn worker. 

## Using

```
$ git clone https://github.com/admiralobvious/falcon-boilerplate.git
$ mv falcon-boilerplate your_app
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r dev_requirements.txt
$ gunicorn -c config.py run:"init_app(env='DEV')" or gunicorn -c config.py run:"init_app(env='PROD')"
```

To run the tests:

```
$ nosetests -v
```
