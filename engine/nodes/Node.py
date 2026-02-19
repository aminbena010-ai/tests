from __future__ import annotations

from collections.abc import Generator
from inspect import signature


class Node:
    def __init__(self, name: str | None = None) -> None:
        self.name = name or self.__class__.__name__
        self.parent: Node | None = None
        self.children: list[Node] = []
        self._ready_called = False
        self._inside_tree = False
        self._ready_callbacks = self._collect_callbacks("_is_ready_callback")
        self._process_callbacks = self._collect_callbacks("_is_process_callback")
        self._input_callbacks = self._collect_callbacks("_is_input_callback")

    def ready(self) -> None:
        pass

    def process(self, dt: float) -> None:
        pass

    def draw(self, screen) -> None:
        pass

    def add_child(self, node: "Node") -> None:
        if node is self:
            raise ValueError("a node cannot be added as a child of itself")
        if node.parent is self:
            return
        if node.parent is not None:
            node.parent.remove_child(node)
        node.parent = self
        self.children.append(node)
        if self._inside_tree:
            node._enter_tree()

    def remove_child(self, node: "Node") -> None:
        if node in self.children:
            self.children.remove(node)
            node.parent = None
            node._set_inside_tree(False)

    def get_node(self, name: str) -> "Node | None":
        for node in self.walk():
            if node.name == name:
                return node
        return None

    def walk(self) -> Generator["Node", None, None]:
        yield self
        for child in self.children:
            yield from child.walk()

    def _collect_callbacks(self, marker: str) -> list:
        callbacks = []
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and getattr(attr, marker, False):
                callbacks.append(attr)
        return callbacks

    def _invoke_callback(self, callback, *args) -> None:
        params_count = len(signature(callback).parameters)
        callback(*args[:params_count])

    def _enter_tree(self) -> None:
        self._inside_tree = True
        if not self._ready_called:
            self.ready()
            for callback in self._ready_callbacks:
                self._invoke_callback(callback)
            self._ready_called = True
        for child in tuple(self.children):
            child._enter_tree()

    def _propagate_process(self, dt: float) -> None:
        for callback in self._input_callbacks:
            self._invoke_callback(callback, dt)
        self.process(dt)
        for callback in self._process_callbacks:
            self._invoke_callback(callback, dt)
        for child in tuple(self.children):
            child._propagate_process(dt)

    def _propagate_draw(self, screen) -> None:
        self.draw(screen)
        for child in tuple(self.children):
            child._propagate_draw(screen)

    def _set_inside_tree(self, value: bool) -> None:
        self._inside_tree = value
        for child in self.children:
            child._set_inside_tree(value)
