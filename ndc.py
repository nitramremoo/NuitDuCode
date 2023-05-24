import pyxel

pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key=pyxel.KEY_P)

xPlayer1 = 10
yPlayer1 = 10
speed = 1

def update():
    
    global xPlayer1, yPlayer1, speed
    
    if (pyxel.btn(pyxel.KEY_UP)):
        yPlayer1 -= 1 * speed
    if (pyxel.btn(pyxel.KEY_DOWN)):
        yPlayer1 += 1 * speed
    if (pyxel.btn(pyxel.KEY_RIGHT)):
        xPlayer1 += 1 * speed
    if (pyxel.btn(pyxel.KEY_LEFT)):
        xPlayer1 -= 1 * speed
    if (pyxel.btn(pyxel.KEY_S)):
        speed += 1
        
def draw():
    pyxel.cls(0)
    pyxel.rect(xPlayer1, yPlayer1, 10, 10, 1)
    
pyxel.run(update, draw)
pyxel.show()
