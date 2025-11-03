from time import perf_counter

def timer(f):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'depth'):
            wrapper.depth = 0
        wrapper.depth += 1

        if wrapper.depth == 1:
            start = perf_counter()
            result = f(*args, **kwargs)
            total_time = perf_counter() - start
            wrapper.depth -= 1
            return result, total_time
        else:
            result = f(*args, **kwargs)
            wrapper.depth -= 1
            return result

    return wrapper