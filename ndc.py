import pyxel

pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key=pyxel.KEY_P)

xPlayer = 10
yPlayer = 10

def update():

    if (pyxel.btn(pyxel.KEY_UP) and y > 0):
        yPlayer -= 1
    if (pyxel.btn(pyxel.KEY_DOWN) and y < 129):
        yPlayer += 1
    if (pyxel.btn(pyxel.KEY_RIGHT) and x < 129):
        xPlayer += 1
    if (pyxel.btn(pyxel.KEY_LEFT) and x > 0):
        xPlayer -= 1
        
def draw():
    pyxel.cls(0)
    pyxel.rect(xPlayer, yPlayer, 10, 10, 2)
    
pyxel.run(update, draw)
