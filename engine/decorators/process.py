def on_process(func):
    func._is_process_callback = True
    return func


__all__ = ["on_process"]
