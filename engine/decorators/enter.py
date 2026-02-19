def on_enter(func):
    func._is_enter_callback = True
    return func


__all__ = ["on_enter"]
