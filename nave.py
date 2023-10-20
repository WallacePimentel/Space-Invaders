from PPlay.sprite import *
from PPlay.window import *

def nave (janela,tecla,player,tiro):

    c = 0
    v = -1000

    if tecla.key_pressed("left"):
        if player.x > 0:
            velocidade_player = -400
            player.x = player.x + velocidade_player * janela.delta_time()

    if tecla.key_pressed("right"):
        if player.x < janela.width - player.width:
            velocidade_player = 400
            player.x = player.x + velocidade_player * janela.delta_time()

    if tiro.y <= 0:
        if tecla.key_pressed("space"):
            tiro.set_position(player.x + player.width / 2, player.y + 10)

    tiro.y = tiro.y + v * janela.delta_time()


    tiro.draw()
    player.draw()