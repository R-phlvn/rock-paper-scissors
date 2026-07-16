from datetime import datetime

def logger(func):
    def wrapped_func(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapped_func



def log_time(func):
    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(f"Total time: {hours}:{minutes}:{seconds}")
        return result
    return wrap_function