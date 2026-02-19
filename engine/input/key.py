from __future__ import annotations

import inspect
from math import sqrt


class KeyInput:
    def __init__(self) -> None:
        self._pressed: set[str] = set()
        self._profiles: dict[str, tuple[str, str, str, str]] = {
            "wasd": ("a", "d", "w", "s"),
            "arrow": ("left", "right", "up", "down"),
        }

    def update_manual(self, keys: set[str]) -> None:
        self._pressed = {k.lower() for k in keys}

    def register_profile(self, name: str, left: str, right: str, up: str, down: str) -> None:
        self._profiles[name.lower()] = (left.lower(), right.lower(), up.lower(), down.lower())

    def update_from_pygame_pressed(self, pressed, pygame_module) -> None:
        mapped = set()
        key_map = {
            "a": pygame_module.K_a,
            "d": pygame_module.K_d,
            "w": pygame_module.K_w,
            "s": pygame_module.K_s,
            "left": pygame_module.K_LEFT,
            "right": pygame_module.K_RIGHT,
            "up": pygame_module.K_UP,
            "down": pygame_module.K_DOWN,
        }
        for name, code in key_map.items():
            if pressed[code]:
                mapped.add(name)
        self._pressed = mapped

    def axis(self, *profiles: str) -> tuple[float, float]:
        if not profiles:
            return 0.0, 0.0
        x = 0.0
        y = 0.0
        for profile in profiles:
            mapped = self._profiles.get(profile.lower())
            if mapped is None:
                raise KeyError(f"input profile '{profile}' is not registered")
            left, right, up, down = mapped
            x += float(right in self._pressed) - float(left in self._pressed)
            y += float(down in self._pressed) - float(up in self._pressed)

        magnitude = sqrt((x * x) + (y * y))
        if magnitude > 0:
            x /= magnitude
            y /= magnitude
        return x, y

    def input(self, *profiles: str) -> tuple[float, float]:
        caller = inspect.currentframe().f_back
        if caller is not None:
            local_scope = caller.f_locals
            if "__module__" in local_scope and "__qualname__" in local_scope:
                local_scope["input_profiles"] = tuple(p.lower() for p in profiles)
                return 0.0, 0.0
        return self.axis(*profiles)


key = KeyInput()

__all__ = ["key", "KeyInput"]
