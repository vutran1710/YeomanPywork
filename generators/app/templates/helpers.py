""" Decorators and Mixins
"""

def deprecated(describe):
    """ Annotation for the deprecated functions
    """
    def decorator(_func):
        def wrapped(*_args, **_kwargs):
            return None

        return wrapped

    return decorator


def shout_err(message: str):
    """ Screaming for Help!!!!
    """
    def decorator(func: Callable):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logger.error('<<< %s >>', message.upper())
                logger.error(err)
                return None

        return wrapped

    return decorator
