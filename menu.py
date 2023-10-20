from PPlay.window import *
from PPlay.sprite import *
import jogar
import dificuldade
import ranking
import sair

janela = Window(700,700)
janela.set_title("Space Invaders - Wallace Pimentel")
janela.set_background_color([0,0,0])
tecla = Window.get_keyboard()
click = Window.get_mouse()

player1 = Sprite("z_player.png")
tiro1 = Sprite("z_tiro.png")
botao_jogar = Sprite("z_jogar.png")
botao_dificuldade = Sprite("z_dificuldade.png")
botao_ranking = Sprite("z_ranking.png")
botao_sair = Sprite("z_sair.png")

while True:
    janela.set_background_color([0,0,0])

    jogar.jogar(janela, tecla, click, botao_jogar,player1,tiro1)
    dificuldade.dif(janela,tecla,click,botao_dificuldade)
    ranking.rank(janela,click,botao_ranking)
    sair.sair(janela,click,botao_sair)

    janela.update()