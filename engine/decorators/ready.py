def on_ready(func):
    func._is_ready_callback = True
    return func


__all__ = ["on_ready"]
