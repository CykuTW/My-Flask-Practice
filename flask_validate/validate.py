from flask import abort


__all__ = ['validate']

def validate(*validators):
    for validator in validators:
        method = getattr(validator, 'validate', None)
        if method is None or not callable(method):
            raise AttributeError('The validator should contains a callable method "def validate(self)"')

    def decorator(func):
        validators
        def func_wrapper(*args, **kwargs):
            for validator in validators:
                if not validator.validate():
                    abort(400)
            return func(*args, **kwargs)
        return func_wrapper
    return decorator
