def trace(f):
    depth = [0]
    
    def wrapper(*args, **kwargs):
        indent = "  " * depth[0]
        args_str = ", ".join([str(arg) for arg in args] + 
                           [f"{k}={v}" for k, v in kwargs.items()])
        print(f"{indent}-> {f.__name__}({args_str})")
        
        depth[0] += 1
        
        try:
            result = f(*args, **kwargs)
            depth[0] -= 1
            print(f"{indent}<- {f.__name__} returned {result}")
            return result
        except Exception as e:
            depth[0] -= 1
            print(f"{indent}<- {f.__name__} raised {type(e).__name__}: {e}")
            raise
    
    return wrapper
