workers = 1
threads = 10
timeout = 120
accesslog = "-"
access_log_format = "url=%(r)s status_code=%(s)s agent=%(a)s request_time_decimal_seconds=%(L)s"
errorlog = "-"
bind = "0.0.0.0:80"
