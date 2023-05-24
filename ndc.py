import pyxel

pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key=pyxel.KEY_P)

xPlayer1 = 10
yPlayer1 = 10
xPlayer2 = 108
yPlayer2 = 10
global_speed = 1

#tirs = []
#tir_coo = []

def update():
    
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, speed
    
    if (pyxel.btn(pyxel.KEY_UP)):
        yPlayer1 -= 1 * global_speed
    if (pyxel.btn(pyxel.KEY_DOWN)):
        yPlayer1 += 1 * global_speed
    if (pyxel.btn(pyxel.KEY_RIGHT)):
        xPlayer1 += 1 * global_speed
    if (pyxel.btn(pyxel.KEY_LEFT)):
        xPlayer1 -= 1 * global_speed
        
    if (pyxel.btn(pyxel.KEY_Z)):
        yPlayer2 -= 1 * global_speed
    if (pyxel.btn(pyxel.KEY_S)):
        yPlayer2 += 1 * global_speed
    if (pyxel.btn(pyxel.KEY_D)):
        xPlayer2 += 1 * global_speed
    if (pyxel.btn(pyxel.KEY_Q)):
        xPlayer2 -= 1 * global_speed
        
def draw():
    pyxel.cls(0)
    pyxel.rect(xPlayer1, yPlayer1, 10, 10, 1)
    pyxel.rect(xPlayer2, yPlayer2, 10, 10, 2)
    
    
pyxel.run(update, draw)
pyxel.show()
