import os
from prometheus_client import multiprocess

#Set Gunicorn Bind Address and Port wsgi
bind = os.getenv("GUNICORN_BIND") or "0.0.0.0:5000"

#Configure Number of Gunicorn Workers:
workers = int(os.getenv("GUNICORN_WORKERS") or 3)

#Configure Gunicorn Maximum Requests:
max_requests = int(os.getenv("GUNICORN_MAX_REQUESTS") or 10**5)

#Configure Gunicorn Maximum Requests Jitter:
max_requests_jitter = int(os.getenv("GUNICORN_MAX_REQUESTS_JITTER") or 100)

#Set Gunicorn Timeout:
timeout = int(os.getenv("GUNICORN_TIMEOUT", "180"))

#Define Child Exit Function for Gunicorn:
def child_exit(server, worker):  # type: ignore
    multiprocess.mark_process_dead(worker.pid)