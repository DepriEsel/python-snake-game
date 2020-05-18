#!/usr/bin/env python
import pyglet

window = pyglet.window.Window(1024,768)


@window.event
def on_draw():
    window.clear()

pyglet.app.run()