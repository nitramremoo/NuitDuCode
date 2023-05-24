import pyxel

global xPlayer = 0
global yPlayer = 0

pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key="pyxel.KEY_P")

def update():
    if (pyxel.btn(pyxel.KEY_UP) and y > 0):
        yPlayer -= 1
    if (pyxel.btn(pyxel.KEY_DOWN) and y < 129):
        yPlayer += 1
    if (pyxel.btn(pyxel.KEY_UP) and x < 129):
        yPlayer += 1
    if (pyxel.btn(pyxel.KEY_UP) and x > 0):
        yPlayer -= 1
