# gunicorn_config.py
bind = "127.0.0.1:8000"  # Replace with the host and port you want to use
workers = 2  # Number of worker processes
timeout = 60  # Set a suitable timeout

