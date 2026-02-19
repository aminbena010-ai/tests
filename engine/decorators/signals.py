def signal(name: str):
    def decorator(func):
        func._signal_name = name
        return func

    return decorator


__all__ = ["signal"]
