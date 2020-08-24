from flask import Flask, g
import logging
import time
from logging.handlers import TimedRotatingFileHandler
from .config import config_by_name
from .model.error_models import Error, NotFoundException

logger = logging.getLogger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    handler = TimedRotatingFileHandler('exam.log', when='midnight')
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s datefmt='))
    logger.addHandler(handler)

    register_interceptors(app)
    register_error_handlers(app)

    return app


def register_interceptors(app):
    @app.before_request
    def before_request_func():
        g.start = time.time()
        logger.info("Starting service")

    @app.after_request
    def after_request_func(response):
        logger.info("Finish service")
        diff = time.time() - g.start
        logger.info(f'Execution time: {diff}')

        return response


def register_error_handlers(app):
    @app.errorhandler(NotFoundException)
    def not_found_error(error):
        """Return a custom not found error message and 404 status code"""
        return {
            "code": 404,
            "name": error.message,
            "description": error.detail_message,
        }

    @app.errorhandler(Exception)
    def internal_error(error):
        """Return a custom of a not expected exception"""
        return {
            "code": 500,
            "name": "Internal error",
            "description": "Oops there was a problem, out engineers may being seeing this in this moment",
        }