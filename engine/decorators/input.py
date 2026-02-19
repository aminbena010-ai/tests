def on_input(func):
    func._is_input_callback = True
    return func


__all__ = ["on_input"]
