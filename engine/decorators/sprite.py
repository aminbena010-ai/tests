def sprite(func):
    func._is_sprite_setup_callback = True
    return func


__all__ = ["sprite"]
