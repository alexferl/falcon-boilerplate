import argparse

from app.util.config import settings

settings = settings

parser = argparse.ArgumentParser(description="Runs the App")

# General
g = parser.add_argument_group("General")
g.add_argument("--app-name", type=str, default="app",
               help="Application and process name (default %(default)s)")
g.add_argument("--env-name", type=str, default="LOCAL",
               choices=["LOCAL", "DEV", "TEST", "STAGING", "PROD"],
               help="Environment to run as (default %(default)s)")
g.add_argument("--environment-variables-prefix", type=str, default="app",
               help="Prefix for environment variables (default %(default)s)")

# Gunicorn
gu = parser.add_argument_group("Gunicorn")
gu.add_argument("--access-log", type=str, default="-",
                help="Where to store Gunicorn access logs (default %(default)s)")
gu.add_argument("--access-log-format", type=str,
                default='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" '
                        '"%(a)s" "%({X-Forwarded-For}i)s" %(L)s',
                help="Gunicorn access log format (default %(default)s)")
gu.add_argument("--bind", type=str, default="127.0.0.1:5000",
                help="The socket to bind. (default %(default)s)")
gu.add_argument("--error-log", type=str, default="-",
                help="Where to store Gunicorn error logs (default %(default)s)")
gu.add_argument("--keep-alive", type=int, default=650,
                help="The number of seconds to wait for requests on a "
                     "Keep-Alive connection. (default %(default)s)")
gu.add_argument("--max-requests", type=int, default=0,
                help="The maximum number of requests a worker will process "
                     "before restarting. (default %(default)s)")
gu.add_argument("--max-requests-jitter", type=int, default=0,
                help="The maximum jitter to add to the max_requests setting. "
                     "(default %(default)s)")
gu.add_argument("--worker-class", type=str,
                default="egg:meinheld#gunicorn_worker",
                help="The type of workers to use. (default %(default)s)")
gu.add_argument("--workers", type=int, default=0,
                help="The number of worker processes for handling requests. "
                     "0 means using the following formula: CPU cores*2+1. "
                     "(default %(default)s)")

# Middleware
m = parser.add_argument_group("Middleware")
m.add_argument("--access-control-allow-origin", type=str, default="*",
               help="(default %(default)s)")
m.add_argument("--access-control-allow-methods", type=str,
               default="GET, PUT, POST, DELETE", help="(default %(default)s)")
m.add_argument("--access-control-allow-credentials", type=str, default="true",
               help="(default %(default)s)")
m.add_argument("--access-control-allow-headers", type=str,
               default="Origin, Authorization, Content-Type, X-Requested-With",
               help="(default %(default)s)")

# Logs
l = parser.add_argument_group("Logs")
fmt = "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
l.add_argument("--log-format", type=str, default=fmt,
               help="Log format (default %(default)s)")
l.add_argument("--log-date-format", type=str, default="%Y-%m-%d %H:%M:%S %z",
               help="Log date format (default %(default)s)")
l.add_argument("--log-handlers", type=str, default="console",
               help="Log handlers (default %(default)s)")
l.add_argument("--log-level", type=str, default="INFO",
               help="Log level (default %(default)s)")
