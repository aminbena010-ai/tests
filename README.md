# your_engine 0.1

Motor educativo 2D inspirado en Godot, escrito en Python.

## Filosofia DX 0.1

- API declarativa y visual.
- Menos boilerplate, mas intencion.
- Nodos familiares (`Node2D`, `Sprite2D`, `Area2D`, `Camera2D`).
- `pygame` oculto dentro del motor.

## Estructura

```text
your_engine/
|-- engine/
|   |-- core/
|   |   |-- Engine.py
|   |   `-- SceneTree.py
|   |-- nodes/
|   |   |-- Node.py
|   |   |-- Node2D.py
|   |   |-- Sprite2D.py
|   |   |-- CharacterBody2D.py
|   |   |-- Area2D.py
|   |   `-- Camera2D.py
|   |-- input/
|   |   `-- key.py
|   |-- decorators/
|   `-- utils/
|-- examples/
|   `-- basic/
|-- assets/
|   `-- sprites/
`-- main.py
```

## Requisitos

- Python 3.10+
- `pygame`

## Ejecutar

1. Instala dependencias:
   `pip install pygame`
2. Ejecuta la demo principal:
   `python main.py`
3. O ejecuta un ejemplo:
   `python examples/basic/example_scene.py`

## API visual

```python
from engine.decorators import on_process, on_ready
from engine.input.key import key
from engine.nodes.Sprite2D import Sprite2D


class Player(Sprite2D):
    texture = "assets/sprites/player.png"
    speed = 300
    key.input("wasd", "arrow")

    @on_ready
    def spawn(self):
        self.x = 120
        self.y = 120

    @on_process
    def animate(self, dt):
        self.rotation += 50 * dt
```

## Nodos incluidos

- `Node`
- `Node2D`
- `Sprite2D`
- `Area2D`
- `Camera2D`
- `CharacterBody2D`
- `AnimatedSprite2D`

## Ejemplo oficial (Node2D + decoradores)

```python
from engine.nodes.Node2D import Node2D
from engine.decorators.characterbody2d import characterbody2d
from engine.decorators.sprite import sprite
from engine.input.key import key


class Player(Node2D):
    speed = 220
    key.input("wasd", "arrow")

    @characterbody2d
    def mov(self, input_axis, dt):
        pass

    @sprite
    def sprint(self):
        self.texture = "assets/sprites/player.png"
```
