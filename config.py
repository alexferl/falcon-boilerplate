bind = '0.0.0.0:5000'
workers = 1
worker_class = 'egg:meinheld#gunicorn_worker'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s" %(L)s'
accesslog = '-'
errorlog = '-'
