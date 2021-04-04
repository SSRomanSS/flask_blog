import logging
import os
from logging.handlers import RotatingFileHandler
from blog import app
from flask.logging import default_handler


_log_format = f"%(asctime)s - [%(levelname)s] - %(pathname)s: def %(funcName)s(line %(lineno)d): %(message)s"


def get_file_handler():
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


app.logger.removeHandler(default_handler)
stream_handler = get_stream_handler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = get_file_handler()
    app.logger.addHandler(file_handler)


# import logging
#
# _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
#
# def get_file_handler():
#     file_handler = logging.FileHandler("x.log")
#     file_handler.setLevel(logging.WARNING)
#     file_handler.setFormatter(logging.Formatter(_log_format))
#     return file_handler
#
# def get_stream_handler():
#     stream_handler = logging.StreamHandler()
#     stream_handler.setLevel(logging.INFO)
#     stream_handler.setFormatter(logging.Formatter(_log_format))
#     return stream_handler
#
# def get_logger(name):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#     logger.addHandler(get_file_handler())
#     logger.addHandler(get_stream_handler())
#     return logger