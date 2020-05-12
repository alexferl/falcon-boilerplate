import argparse

from app.util.config import settings

settings = settings

parser = argparse.ArgumentParser(description="Runs the App")

# General
g = parser.add_argument_group("General")
g.add_argument(
    "--app-name",
    type=str,
    default="app",
    help="Application and process name (default %(default)s)",
)
g.add_argument(
    "--env-name",
    type=str,
    default="LOCAL",
    choices=["LOCAL", "DEV", "TEST", "STAGING", "PROD"],
    help="Environment to run as (default %(default)s)",
)
g.add_argument(
    "--environment-variables-prefix",
    type=str,
    default="app",
    help="Prefix for environment variables (default %(default)s)",
)

# See rapidjson's docs (https://python-rapidjson.readthedocs.io/en/latest/api.html)
# for the following settings:

g.add_argument(
    "--json-number-mode",
    type=str,
    default=None,
    help="Enable particular behaviors in handling numbers (default %(default)s)",
)
g.add_argument(
    "--json-datetime-mode",
    type=str,
    default=None,
    help="How should datetime, time and date instances be handled (default %(default)s)",
)
g.add_argument(
    "--json-uuid-mode",
    type=str,
    default=None,
    help="How should UUID instances be handled (default %(default)s)",
)

# Gunicorn
gu = parser.add_argument_group("Gunicorn")
gu.add_argument(
    "--access-log",
    type=str,
    default="-",
    help="Where to store Gunicorn access logs (default %(default)s)",
)
gu.add_argument(
    "--access-log-format",
    type=str,
    default='%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" '
    '"%(a)s" "%({X-Forwarded-For}i)s" %(L)s',
    help="Gunicorn access log format (default %(default)s)",
)
gu.add_argument(
    "--bind",
    type=str,
    default="127.0.0.1:5000",
    help="The socket to bind. (default %(default)s)",
)
gu.add_argument(
    "--error-log",
    type=str,
    default="-",
    help="Where to store Gunicorn error logs (default %(default)s)",
)
gu.add_argument(
    "--keep-alive",
    type=int,
    default=650,
    help="The number of seconds to wait for requests on a "
    "Keep-Alive connection. (default %(default)s)",
)
gu.add_argument(
    "--max-requests",
    type=int,
    default=0,
    help="The maximum number of requests a worker will process "
    "before restarting. (default %(default)s)",
)
gu.add_argument(
    "--max-requests-jitter",
    type=int,
    default=0,
    help="The maximum jitter to add to the max_requests setting. "
    "(default %(default)s)",
)
gu.add_argument(
    "--worker-class",
    type=str,
    default="egg:meinheld#gunicorn_worker",
    help="The type of workers to use. (default %(default)s)",
)
gu.add_argument(
    "--workers",
    type=int,
    default=0,
    help="The number of worker processes for handling requests. "
    "0 means using the following formula: CPU cores*2+1. "
    "(default %(default)s)",
)

# Middleware
m = parser.add_argument_group("Middleware")
m.add_argument(
    "--cors-enabled",
    default=False,
    action="store_true",
    help="Enable cross-origin resource sharing (default %(default)s)",
)
m.add_argument(
    "--cors-allow-origins",
    type=str,
    default="*",
    help="List of origins that may access the resource. (default %(default)s)",
)
m.add_argument(
    "--cors-allow-methods",
    type=str,
    default="GET, HEAD, PUT, PATCH, POST, DELETE",
    help="List methods allowed when accessing the resource. This is used in response to a preflight request. (default %(default)s)",
)
m.add_argument(
    "--cors-allow-headers",
    type=str,
    default="",
    help="List of request headers that can be used when making the actual request. This is in response to a preflight request. (default %(default)s)",
)
m.add_argument(
    "--cors-allow-credentials",
    default=False,
    action="store_true",
    help="Indicates whether or not the response to the request can be exposed. (default %(default)s)",
)
m.add_argument(
    "--cors-expose-headers",
    type=str,
    default="",
    help="Defines a whitelist headers that clients are allowed to access. (default %(default)s)",
)
m.add_argument(
    "--cors-max-age",
    type=int,
    default=0,
    help="Indicates how long (in seconds) the results of a preflight request can be cached. (default %(default)s)",
)

# Logs
l = parser.add_argument_group("Logs")
fmt = "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
l.add_argument(
    "--log-format", type=str, default=fmt, help="Log format (default %(default)s)"
)
l.add_argument(
    "--log-date-format",
    type=str,
    default="%Y-%m-%d %H:%M:%S %z",
    help="Log date format (default %(default)s)",
)
l.add_argument(
    "--log-handlers",
    type=str,
    default="console",
    help="Log handlers (default %(default)s)",
)
l.add_argument(
    "--log-level", type=str, default="INFO", help="Log level (default %(default)s)"
)
