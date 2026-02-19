from engine.core.Engine import Engine
from examples.basic.example_scene import build_scene


def main() -> None:
    root = build_scene()
    Engine(root).run()


if __name__ == "__main__":
    main()
