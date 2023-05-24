import pyxel

# initialization
pyxel.init(128, 128, title="Nuit Du Code", fps=30, quit_key=pyxel.KEY_P)

# x position of first player
xPlayer1 = 108
# y position of first player
yPlayer1 = 10
# global factor of first player
factorPlayer1 = 1
# x position of second player
xPlayer2 = 10
# y position of second player
yPlayer2 = 10
# global factor of second player
factorPlayer2 = 1
# game speed
global_speed = 1
# top right corner
def ctr(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return ((xPlayer1+7)//8)
        if (x_or_y == "y"):
            return ((yPlayer1//8))
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return ((xPlayer2+7)//8)
        if (x_or_y == "y"):
            return ((yPlayer2//8))
# top left corner
def ctl(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return (xPlayer1//8)
        if (x_or_y == "y"):
            return (yPlayer1//8)
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return (xPlayer2//8)
        if (x_or_y == "y"):
            return (yPlayer2//8)
# bottom right corner
def cbr(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return ((xPlayer1+7)//8)
        if (x_or_y == "y"):
            return ((yPlayer1+7)//8)
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return ((xPlayer2+7)//8)
        if (x_or_y == "y"):
            return ((yPlayer2+7)//8)
# bottom left corner
def cbl(PLAYER, x_or_y):
    if (PLAYER == "PLAYER_1"):
        if (x_or_y == "x"):
            return (xPlayer1//8)
        if (x_or_y == "y"):
            return ((yPlayer1+7)//8)
    if (PLAYER == "PLAYER_2"):
        if (x_or_y == "x"):
            return (xPlayer2//8)
        if (x_or_y == "y"):
            return ((yPlayer2+7)//8)
            
            

# function update()
def update():
    
    # import global variables
    global xPlayer1, yPlayer1, xPlayer2, yPlayer2, factorPlayer1, factorPlayer2, global_speed
    
    """display variables for debug"""
    
    # go up for player 1
    if (pyxel.btn(pyxel.KEY_UP)):
        yPlayer1 -= 1 * global_speed
    # go down for player 1
    if (pyxel.btn(pyxel.KEY_DOWN)):
        yPlayer1 += 1 * global_speed
    # go right for player 1
    if (pyxel.btn(pyxel.KEY_RIGHT)):
        xPlayer1 += 1 * global_speed
    # go left for player 1
    if (pyxel.btn(pyxel.KEY_LEFT)):
        xPlayer1 -= 1 * global_speed
    # attack for player 1
    if (pyxel.btn(pyxel.KEY_KP_0)):
        #^^^^^^animation here^^^^^^
        if((pyxel.pget(ctr("PLAYER_1", "x"), ctr("PLAYER_1", "y")) == 2) or (pyxel.pget(ctl("PLAYER_1", "x"), ctl("PLAYER_1", "y")) == 2) or (pyxel.pget(cbr("PLAYER_1", "x"), cbr("PLAYER_1", "y")) == 2) or (pyxel.pget(cbl("PLAYER_1", "x"), cbl("PLAYER_1", "y")) == 2)):
                punch("PLAYER_2")
        
    # go up for player 2
    if (pyxel.btn(pyxel.KEY_Z)):
        yPlayer2 -= 1 * global_speed
    # go down for player 2
    if (pyxel.btn(pyxel.KEY_S)):
        yPlayer2 += 1 * global_speed
    # go right for player 2
    if (pyxel.btn(pyxel.KEY_D)):
        xPlayer2 += 1 * global_speed
    # go left for player 2
    if (pyxel.btn(pyxel.KEY_Q)):
        xPlayer2 -= 1 * global_speed
    # punch for player 2
    if (pyxel.btn(pyxel.KEY_SPACE)):
        print("succes2")
         #^^^^^^animation here^^^^^^
        if( (pyxel.pget(ctr("PLAYER_2", "x"), ctr("PLAYER_2", "y")) == 1) or (pyxel.pget(ctl("PLAYER_2", "x"), ctl("PLAYER_2", "y")) == 1) or (pyxel.pget(cbr("PLAYER_2", "x"), cbr("PLAYER_2", "y")) == 1) or (pyxel.pget(cbl("PLAYER_2", "x"), cbl("PLAYER_2", "y")) == 1)):
                print("Succes")
                punch("PLAYER_1")
       
# show characters with draw()
def draw():
    global factorPlayer1, factorPlayer2, xPlayer1, yPlayer1, xPlayer2, yPlayer2
    
    pyxel.cls(0)
    pyxel.rect(xPlayer1, yPlayer1, (10 * factorPlayer1), (10 * factorPlayer1), 1)
    pyxel.rect(xPlayer2, yPlayer2, (10 * factorPlayer2), (10 * factorPlayer2), 2)
    
# attack function
def punch(player):
    
    global factorPlayer1, factorPlayer2
    
    if (player == "PLAYER_2"):
        factorPlayer2 -= 0.2 * factorPlayer1
        factorPlayer1 += 0.1
    if (player == "PLAYER_1"):
        factorPlayer1 -= 0.2 * factorPlayer2
        factorPlayer2 += 0.1

# run game
pyxel.run(update, draw)
# update screen
pyxel.show()
