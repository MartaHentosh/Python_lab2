"""
This module provides decorator for logging
"""
import logging


def logged(exception, mode):
    """
    Create a decorator for logging exceptions.
    This decorator allows you to log exceptions that occur within a function.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except exception as exception_instance:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    logger.addHandler(logging.StreamHandler())
                elif mode == "file":
                    logger.addHandler(logging.FileHandler("exception.log"))
                logger.exception(exception_instance)

                return None

        return wrapper

    return decorator
